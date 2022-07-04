
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session
from asyncio import current_task

import os

async_engine = create_async_engine(os.environ.get('DB_URL','sqlite+aiosqlite:///dal/bands.db'))
async_session_factory = sessionmaker(async_engine, class_=AsyncSession,expire_on_commit=False)

class BaseDAL:

    def __init__(self):
        AsyncScopedSession = async_scoped_session(async_session_factory, scopefunc=current_task)
        self.session = AsyncScopedSession()