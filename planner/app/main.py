from fastapi import FastAPI
from app.routes.session import router as session_router
from app.routes.posts import router as posts_router
from app.routes.comments import router as comments_router
from app.routes.calendar import router as calendar_router
from app.routes.users import router as users_router


app = FastAPI(title="Content Planner API")
app.include_router(session_router, prefix="/api")
app.include_router(posts_router, prefix="/api")
app.include_router(comments_router, prefix="/api")
app.include_router(calendar_router, prefix="/api")
app.include_router(users_router, prefix="/api")