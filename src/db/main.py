
from cgitb import text
from sqlmodel import create_engine
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

engine = AsyncEngine(create_engine(
    url=Config.DATABASE_URL,
    echo = True
))


async def initdb():
    """create a connection to our db"""

    async with engine.begin() as conn:
        statement = text("select 'Hello World'")

        result = await conn.execute(statement)

        print(result.all())