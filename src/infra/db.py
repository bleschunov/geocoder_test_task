import os
from typing import AsyncIterator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection

con_string = os.getenv("DB_CONNECTION_STRING")
engine = create_async_engine(con_string, pool_size=20)


async def get_conn() -> AsyncIterator[AsyncConnection]:
    async with engine.begin() as conn:
        yield conn
