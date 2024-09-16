
from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import initdb


#the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):    
    await initdb()
    yield
    print("server is stopping")



app = FastAPI(
    lifespan=lifespan # add the lifespan event to our application
)

app.include_router(
    book_router,
    prefix="/books",
    tags=['books']
)