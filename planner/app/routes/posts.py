from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime

router = APIRouter(prefix="/posts", tags=["posts"])

class PostIn(BaseModel):
    title: str | None = None
    text: str | None = None
    planned_at: datetime | None = None
    timezone: str | None = None
    category_id: int | None = None
    tags: list[str] = Field(default_factory=list)
    status: str = "draft"


@router.post("")
async def create_post(data: PostIn):
    # TODO: сохранить в БД, вернуть объект
    return {"id": 1, **data.model_dump()}


@router.get("")
async def list_posts(status: str | None = None):
    # TODO: фильтрация по статусу/дате/категории
    return []


@router.get("/{post_id}")
async def get_post(post_id: int):
    # TODO: получить из БД
    return {"id": post_id}


@router.put("/{post_id}")
async def update_post(post_id: int, data: PostIn):
    # TODO: обновить
    return {"id": post_id, **data.model_dump()}


@router.delete("/{post_id}")
async def delete_post(post_id: int):
    # TODO: удалить
    return {"ok": True}