from fastapi import APIRouter
from datetime import date

router = APIRouter(prefix="/calendar", tags=["calendar"])

@router.get("/range")
async def calendar_range(start: date, end: date):
    # TODO: вернуть посты за период (для календаря)
    return []