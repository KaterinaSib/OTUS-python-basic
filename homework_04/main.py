"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
import logging

from jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL
from models import Base, User, Post, async_engine, db_session

from common import configure_logging

log = logging.getLogger(__name__)


async def created_db_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def save_user_in_db(user_data):
    async with db_session() as session:
        async with session.begin():
            for user in user_data:
                name = user["name"]
                username = user["username"]
                email = user["email"]
                user = User(name=name, username=username, email=email)
                session.add(user)
            await session.commit()


async def save_post_in_db(post_data):
    async with db_session() as session:
        async with session.begin():
            for post in post_data:
                user_id = post["userId"]
                title = post["title"]
                body = post["body"]
                post = Post(user_id=user_id, title=title, body=body)
                session.add(post)
            await session.commit()


async def async_main():
    configure_logging()
    await created_db_tables()
    log.info("drop and create all tables")
    user_data, post_data = await asyncio.gather(
        fetch_json(USERS_DATA_URL), fetch_json(POSTS_DATA_URL)
    )
    log.info("user_data: %s", user_data)
    log.info("post_data: %s", post_data)
    await save_user_in_db(user_data)
    log.info("save_users")
    await save_post_in_db(post_data)
    log.info("save_posts")


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
