import os
from pydantic import BaseModel

class SystemConfig(BaseModel):
    APP_NAME: str = "NEXUS-TRAP C4ISR"
    APP_VERSION: str = "2.0.0-MIL"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # OT Decoy Configuration (Modbus TCP)
    MODBUS_HOST: str = os.getenv("MODBUS_HOST", "0.0.0.0")
    MODBUS_PORT: int = int(os.getenv("MODBUS_PORT", "5020"))  # Default 5020 for unprivileged dev; 502 in Docker/root
    
    # DNS Canary Listener Configuration
    DNS_HOST: str = os.getenv("DNS_HOST", "0.0.0.0")
    DNS_PORT: int = int(os.getenv("DNS_PORT", "5053"))        # Default 5053 for dev; 53 in Docker/root
    CANARY_DOMAIN: str = os.getenv("CANARY_DOMAIN", "canary.nexustrap.mil.id")
    
    # Security & Anti-Backfire Protections
    MAX_TARPIT_PER_IP: int = 64        # Prevents single attacker from exhausting descriptors
    MAX_GLOBAL_TARPIT: int = 1000      # Global connection ceiling
    IMMUNE_IPS: list[str] = [
        "127.0.0.1", "::1", "10.0.0.1", "192.168.1.1", "192.168.0.1"  # Gateway & Loopback protection
    ]
    
    # AI Sitrep (Local SLM)
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3:8b")

settings = SystemConfig()
