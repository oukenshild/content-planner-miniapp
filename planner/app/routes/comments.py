from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime


router = APIRouter(prefix="/comments", tags=["comments"])


class CommentIn(BaseModel):
    post_id: int
    text: str


@router.post("")
async def add_comment(data: CommentIn):
    # TODO: сохранить в БД
    return {"id": 1, "created_at": datetime.utcnow().isoformat(), **data.model_dump()}