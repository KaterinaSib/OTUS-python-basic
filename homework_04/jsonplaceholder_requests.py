"""
Создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import asyncio
import logging

import aiohttp
from common import configure_logging

log = logging.getLogger(__name__)

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str, params: dict | None = None) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.json()


async def main():
    configure_logging()
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_json(USERS_DATA_URL))
        task2 = tg.create_task(fetch_json(POSTS_DATA_URL))
    log.info("Fetched json from user_data (1): %s", task1.result())
    log.info("Fetched json from posts_data (2): %s", task2.result())


if __name__ == '__main__':
    asyncio.run(main())
