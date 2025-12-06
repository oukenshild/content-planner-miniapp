from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.auth import verify_init_data

router = APIRouter()

class SessionIn(BaseModel):
    initData: str


@router.post("/session")
async def create_session(payload: SessionIn):
    if not verify_init_data(payload.initData):
        raise HTTPException(401, "invalid initData")
    return {"ok": True}