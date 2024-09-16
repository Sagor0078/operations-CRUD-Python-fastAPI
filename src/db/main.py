
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.config import Config

# Create an async engine
engine = create_async_engine(
    Config.DATABASE_URL,
    echo=True
)

# Create a session factory
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def initdb():
    async with engine.begin() as conn:
        # Your database initialization logic here
        statement = text("SELECT 'Hello World'")

        result = await conn.execute(statement)

        print(result.all())


