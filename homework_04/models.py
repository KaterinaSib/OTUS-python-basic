"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, declared_attr, relationship
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Text,
)

PG_CONN_URI = (os.environ.get("SQLALCHEMY_PG_CONN_URI") or
               "postgresql+asyncpg://user:example@localhost/blog")

async_engine = create_async_engine(PG_CONN_URI, echo=False)

async_session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)

db_session = async_sessionmaker(
    bind=async_engine,
    autocommit=False,
    expire_on_commit=False,
)

Session = async_session


class Base(DeclarativeBase):

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


class User(Base):

    name = Column(String(200), nullable=False, unique=False)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    posts = relationship(
        # to class name
        "Post",
        # how to access to this model[s]: post.`author`
        back_populates="author",
        # user can have any number of posts
        uselist=True,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"name={self.name!r}, "
            f"username={self.username!r}, "
            f"email={self.email!r}"
            f")"
        )


class Post(Base):

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )
    title = Column(
        String(80),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(Text, default="", server_default="")

    author = relationship(
        # to class name
        "User",
        # how to access to this model[s]: user.`posts`
        back_populates="posts",
        # author can be only one due to single `user_id`
        uselist=False,
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"user_id={self.user_id}, "
            f"title={self.title!r}, "
            f"body={self.body!r}"
            f")"
        )
