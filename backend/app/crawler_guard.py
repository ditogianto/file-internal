"""
NEXUS-TRAP // PUSSIBERAD TNI AD
Crawler Discrimination & Anti-Spoofing Guard Engine

Fungsi:
1. Membedakan bot crawler legal (Googlebot, Bingbot, YandexBot, Applebot, Baiduspider) vs. offensive scanner (Gobuster, Nmap, SQLmap).
2. Mencegah false positive / false attribution pada mesin pencari legal.
3. Mendeteksi "Crawler Spoofing / Mimicry Attack": Penyerang yang memalsukan User-Agent Googlebot untuk mengelabui WAF/Honeypot,
   diverifikasi secara forensik menggunakan FCrDNS (Forward-Confirmed reverse DNS).
"""

import socket
import asyncio
import re
import ipaddress
from typing import Tuple, Dict, Any, Optional
from fastapi import Request

# In-memory DNS cache with TTL / memoization to prevent latency bottlenecks
_dns_cache: Dict[str, Tuple[str, bool]] = {}

LEGITIMATE_CRAWLER_PATTERNS = {
    "google": {
        "ua_tokens": ["googlebot", "google-inspectiontool", "mediapartners-google", "adsbot-google"],
        "domains": [".googlebot.com", ".google.com"]
    },
    "bing": {
        "ua_tokens": ["bingbot", "msnbot", "bingpreview"],
        "domains": [".search.msn.com", ".bing.com"]
    },
    "yandex": {
        "ua_tokens": ["yandexbot", "yandeximages", "yandexaccessibilitybot"],
        "domains": [".yandex.com", ".yandex.ru", ".yandex.net"]
    },
    "apple": {
        "ua_tokens": ["applebot"],
        "domains": [".applebot.apple.com", ".apple.com"]
    },
    "duckduckgo": {
        "ua_tokens": ["duckduckbot", "duckduckgo-favicons-bot"],
        "domains": [".duckduckgo.com"]
    },
    "baidu": {
        "ua_tokens": ["baiduspider"],
        "domains": [".baidu.com", ".baidu.jp"]
    }
}

OFFENSIVE_TOOL_TOKENS = [
    "gobuster", "dirsearch", "sqlmap", "nmap", "nikto", "wpscan",
    "hydra", "masscan", "zgrab", "burpcollaborator", "feroxbuster",
    "ffuf", "wfuzz", "acunetix", "nessus", "metasploit"
]

async def verify_fcrdns_async(ip: str, valid_domains: list) -> Tuple[bool, str]:
    """
    Performs Forward-Confirmed reverse DNS (FCrDNS) verification.
    1. Reverse DNS: IP -> Hostname
    2. Check if Hostname ends with an official search engine domain
    3. Forward DNS: Hostname -> IP (confirms authenticity)
    """
    # Strict IP validation to prevent NetBIOS/DNS hang on non-IP hostnames
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_loopback or ip_obj.is_private or ip_obj.is_multicast or ip_obj.is_reserved:
            return False, "INTERNAL_OR_LOOPBACK"
    except ValueError:
        return False, "INVALID_IP_FORMAT"

    loop = asyncio.get_running_loop()

    def _sync_lookup():
        try:
            # 1. Reverse lookup
            host, _, _ = socket.gethostbyaddr(ip)
            host = host.lower()
            
            # Check domain match
            matches_domain = any(host.endswith(dom.lower()) for dom in valid_domains)
            if not matches_domain:
                return False, host
                
            # 2. Forward lookup to confirm no PTR poisoning (supports multi-A record clusters)
            addr_info = socket.getaddrinfo(host, None)
            resolved_ips = {item[4][0] for item in addr_info}
            if ip in resolved_ips:
                return True, host
            return False, host
        except Exception:
            return False, "LOOKUP_FAILED"

    return await loop.run_in_executor(None, _sync_lookup)

async def classify_request(request: Request) -> Dict[str, Any]:
    """
    Classifies an incoming request into one of:
    - BENIGN_CRAWLER: Genuine verified search engine crawler (Googlebot, Bingbot, etc.)
    - SPOOFED_CRAWLER: Adversary forging User-Agent as Googlebot/Bingbot to evade detection!
    - OFFENSIVE_SCANNER: Known reconnaissance scanner (Gobuster, Nmap, SQLmap, etc.)
    - HEADLESS_AUTOMATION: Scripted client (Python-requests, curl, etc.)
    - REGULAR_CLIENT: Normal browser / interactive user
    """
    raw_host = request.client.host if request.client else "UNKNOWN"
    forwarded = request.headers.get("x-forwarded-for")
    if raw_host in ["127.0.0.1", "::1", "localhost", "testclient"] and forwarded:
        client_ip = forwarded.split(",")[0].strip()
    else:
        client_ip = raw_host
    user_agent = request.headers.get("user-agent", "").lower()
    
    # 1. Check if user-agent claims to be a search engine bot
    claimed_provider = None
    matched_config = None
    for provider, cfg in LEGITIMATE_CRAWLER_PATTERNS.items():
        if any(token in user_agent for token in cfg["ua_tokens"]):
            claimed_provider = provider
            matched_config = cfg
            break

    if claimed_provider:
        # Check cache first
        if client_ip in _dns_cache:
            verified, rdns_host = _dns_cache[client_ip]
        else:
            try:
                # 1.5s timeout for DNS check to avoid blocking
                verified, rdns_host = await asyncio.wait_for(
                    verify_fcrdns_async(client_ip, matched_config["domains"]),
                    timeout=1.5
                )
            except Exception:
                verified, rdns_host = False, "DNS_TIMEOUT"
            
            _dns_cache[client_ip] = (verified, rdns_host)

        if verified:
            return {
                "category": "BENIGN_CRAWLER",
                "provider": claimed_provider,
                "verified": True,
                "hostname": rdns_host,
                "user_agent": user_agent,
                "is_adversary": False,
                "reason": f"Legitimate {claimed_provider.title()} crawler verified via FCrDNS ({rdns_host})"
            }
        else:
            return {
                "category": "SPOOFED_CRAWLER",
                "provider": claimed_provider,
                "verified": False,
                "hostname": rdns_host,
                "user_agent": user_agent,
                "is_adversary": True,
                "reason": f"MIMICRY ATTACK: Client claims {claimed_provider.title()} but rDNS check failed (rDNS: {rdns_host})"
            }

    # 2. Check for known offensive tools
    for token in OFFENSIVE_TOOL_TOKENS:
        if token in user_agent:
            return {
                "category": "OFFENSIVE_SCANNER",
                "tool": token,
                "user_agent": user_agent,
                "is_adversary": True,
                "reason": f"Known offensive security tool signature: {token}"
            }

    # 3. Check for general headless scripting tools
    if any(h in user_agent for h in ["python-requests", "curl/", "libwww-perl", "aiohttp", "urllib"]):
        return {
            "category": "HEADLESS_AUTOMATION",
            "tool": user_agent.split('/')[0] if '/' in user_agent else user_agent[:16],
            "user_agent": user_agent,
            "is_adversary": True,
            "reason": "Scripted headless HTTP client scanning decoy endpoints"
        }

    # 4. Standard interactive browser / client
    return {
        "category": "REGULAR_CLIENT",
        "user_agent": user_agent,
        "is_adversary": False,
        "reason": "Standard browser client"
    }

def get_robots_txt_content() -> str:
    """Returns RFC 9309 compliant robots.txt with active honeypot isolation."""
    return """# ==============================================================================
# PUSSIBERAD TNI AD - MILITARY ACTIVE CYBER DEFENSE PERIMETER
# ROBOTS DISALLOW RULES & DECEPTION BOUNDARY SPECIFICATION (RFC 9309)
# ==============================================================================
# Legal Search Engine Crawlers (Googlebot, Bingbot, Applebot, etc.):
# You are strictly prohibited from indexing internal military portals and honeypots.
# Compliance with this document ensures exclusion from defensive countermeasures.
# 
# WARNING TO ADVERSARIES:
# Unauthorized access to Disallow directives by automated scanners or masqueraded
# crawlers will be flagged as intentional military reconnaissance under UU ITE & KUHP.
# ==============================================================================

User-agent: *
Disallow: /decoy-portal/
Disallow: /decoy-portal/api/
Disallow: /api/
Disallow: /.env
Disallow: /config.env
Disallow: /backup.sql
Disallow: /database.sql
Disallow: /download/
Disallow: /canary-qr
Disallow: /ws/

# Perimeter Defense Contact: cert@pussiberad.mil.id
"""
