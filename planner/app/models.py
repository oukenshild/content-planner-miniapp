from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, DateTime, Boolean, JSON, Text, Enum, Table
from datetime import datetime
import enum

class Base(DeclarativeBase):
    pass

class Role(enum.StrEnum):
    OWNER = "owner"
    EDITOR = "editor"
    VIEWER = "viewer"


class Status(enum.StrEnum):
    DRAFT = "draft"
    PENDING = "pending" # на согласовании
    APPROVED = "approved" # утверждено
    PUBLISHED = "published" # вручную опубликовано
    ARCHIVED = "archived"


post_tags = Table(
    "post_tags", Base.metadata,
    mapped_column("post_id", ForeignKey("posts.id"), primary_key=True),
    mapped_column("tag_id", ForeignKey("tags.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tg_user_id: Mapped[int] = mapped_column(Integer, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    username: Mapped[str | None] = mapped_column(String(255))
    role: Mapped[Role] = mapped_column(Enum(Role), default=Role.EDITOR)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)


class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str | None] = mapped_column(String(255))
    text: Mapped[str | None] = mapped_column(Text)
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.DRAFT)
    planned_at: Mapped[datetime | None] = mapped_column(DateTime, index=True)
    timezone: Mapped[str | None] = mapped_column(String(64))
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"))
    attachments: Mapped[dict | None] = mapped_column(JSON) # ссылки на файлы/медиа
    meta: Mapped[dict | None] = mapped_column(JSON) # произвольные поля (UTM, площадка и т.п.)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)