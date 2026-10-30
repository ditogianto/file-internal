import uvicorn
from app.config import settings

if __name__ == "__main__":
    print(f"[*] Menyalakan Backend NEXUS-TRAP C4ISR pada http://{settings.HOST}:{settings.PORT}")
    print(f"[*] OT Modbus Daemon port : {settings.MODBUS_PORT}")
    print(f"[*] DNS Canary Listener   : UDP {settings.DNS_PORT}")
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=False)
