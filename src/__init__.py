

from fastapi import FastAPI
from src.books.routes import book_router

version = 'v1'

app = FastAPI(
    title="Bookly",
    description="A REST API for a book review web service",
    version= version,
    lifespan=life_span
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=['books'])