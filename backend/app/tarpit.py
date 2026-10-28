import os
import asyncio
import random
from typing import AsyncGenerator, Dict
from fastapi import Request
from fastapi.responses import StreamingResponse, Response
from app.config import settings
from app.telemetry import telemetry

# Drip rate interval: default 2.0s in demo/lab for fast timeout demonstrations, configurable to 15.0s
TARPIT_DRIP_INTERVAL = float(os.getenv("TARPIT_DRIP_INTERVAL", "2.0"))

# Active socket count per IP to prevent Self-DoS from botnets
active_ip_conns: Dict[str, int] = {}
ip_lock = asyncio.Lock()

async def infinite_chunk_generator(client_ip: str) -> AsyncGenerator[bytes, None]:
    """Generates an infinite chunked stream at an agonizingly slow drip rate (1 byte/chunk).
    Causes scanner threads (Gobuster, Nmap, Dirsearch) to lock up completely.
    Includes memory leak and connection exhaustion guards."""
    
    async with ip_lock:
        active_ip_conns[client_ip] = active_ip_conns.get(client_ip, 0) + 1

    await telemetry.increment_thread_lock(1)
    await telemetry.add_log(
        level="WARN",
        tag="TARPIT",
        message=f"Scanner thread dari {client_ip} TERKUNCI dalam Sticky Tarpit Chunk.",
        source_ip=client_ip
    )
    
    noise = b"TNI-AD-NEXUS-TRAP-INTERCEPT-ACTIVE-"
    try:
        while True:
            # Check if tarpit is still active
            if not telemetry.tarpit_active:
                yield b"\n[TARPIT DEACTIVATED BY OPERATOR]\n"
                break
            
            # Send small chunk then sleep to tie down thread
            byte_val = bytes([noise[random.randint(0, len(noise) - 1)]])
            yield byte_val
            await asyncio.sleep(2.0)
    except (asyncio.CancelledError, ConnectionResetError, ConnectionAbortedError, BrokenPipeError, OSError):
        pass
    finally:
        # Attacker client disconnected or killed
        async with ip_lock:
            if client_ip in active_ip_conns:
                active_ip_conns[client_ip] -= 1
                if active_ip_conns[client_ip] <= 0:
                    del active_ip_conns[client_ip]
        if telemetry.locked_threads > 0:
            await telemetry.increment_thread_lock(-1)

def execute_tarpit_response(request: Request) -> Response:
    """Wraps the chunked generator in a FastAPI StreamingResponse with Anti-Backfire Guards."""
    client_ip = request.client.host if request.client else "UNKNOWN"

    # Anti-Backfire Guard 1: Immune IPs (Gateways, Loopback, Command Consoles) cannot be tarpitted
    if client_ip in settings.IMMUNE_IPS:
        return Response(status_code=200, content="[IMMUNE_WHITELIST_BYPASS]")

    # Anti-Backfire Guard 2: Capping per IP to prevent attacker from intentionally exhausting server sockets
    current_ip_conns = active_ip_conns.get(client_ip, 0)
    if current_ip_conns >= settings.MAX_TARPIT_PER_IP:
        # Instantly close connection to protect defense server's socket descriptor pool
        return Response(status_code=429, content="Rate limit threshold reached.")

    # Anti-Backfire Guard 3: Global ceiling check
    if telemetry.locked_threads >= settings.MAX_GLOBAL_TARPIT:
        return Response(status_code=503, content="Global tarpit ceiling reached.")

    return StreamingResponse(
        infinite_chunk_generator(client_ip),
        media_type="application/octet-stream",
        headers={
            "X-Tarpit-Interdiction": "ACTIVE-NEXUS-TRAP",
            "Transfer-Encoding": "chunked",
            "Cache-Control": "no-cache, no-store, must-revalidate"
        }
    )
