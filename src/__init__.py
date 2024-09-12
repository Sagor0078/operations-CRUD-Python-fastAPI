from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict
from src.books.routes import book_router

version = 'v1'

async def life_span(app: FastAPI):
    # Code to be executed before the application starts
    yield
    # Code to be executed after the application shuts down

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version=version,
    lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])

