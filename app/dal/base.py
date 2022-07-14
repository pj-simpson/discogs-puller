from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session
from asyncio import current_task
from sqlalchemy.engine.result import ChunkedIteratorResult

import typing


import os

async_engine = create_async_engine(
    os.environ.get("DB_URL", "sqlite+aiosqlite:///dal/bands.db")
)
async_session_factory = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


class BaseDAL:
    def __init__(self) -> None:
        AsyncScopedSession = async_scoped_session(
            async_session_factory, scopefunc=current_task
        )
        self.session = AsyncScopedSession()

    async def _get_one_object_from_result(
        self, result: ChunkedIteratorResult, table_name: str
    ) -> typing.Dict:
        # get the row_mapping
        # <class 'sqlalchemy.engine.row.RowMapping'>
        rows = result.mappings().one()
        # pop out the single row
        single_row = rows[table_name]
        return single_row.resp_for_json()

    async def _build_object_list_from_result(
        self, result: ChunkedIteratorResult, table_name: str
    ) -> typing.List:
        rows = result.mappings().all()
        object_list = []
        for row in rows:
            item = row[table_name]
            object_list.append(item.resp_for_json())
        return object_list
