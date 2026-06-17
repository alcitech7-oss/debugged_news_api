from fastapi import Header, HTTPException
from quantex.settings import settings

async def verify_secret(x_secret: str = Header(None)):
    if x_secret is None or x_secret != settings.secret_key:
        raise HTTPException(status_code=403, detail="Secret header invalid")