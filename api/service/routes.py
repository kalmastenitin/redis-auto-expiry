from datetime import timedelta
from wsgiref import headers
from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from api import redis
import uuid
from datetime import timedelta

router = APIRouter()


@router.post("/login")
async def login(username: str = Header(...), password: str = Header(...)):
    if username == "admin" and password == "admin":
        session_id = str(uuid.uuid4())
        print(dir(redis))
        await redis.execute_command('set', session_id, "encrypted_secret_data", 'ex', 30)
    return JSONResponse({"details": session_id})


@router.get("/session")
async def validate(sessionId: str):
    print(await redis.exists(sessionId))
    if not await redis.exists(sessionId):
        return JSONResponse({"details": "expired"}, status_code=401)
    return JSONResponse({"details": "success"})
