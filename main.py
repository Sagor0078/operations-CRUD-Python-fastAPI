from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
async def read_root():
    return {"message": "Hello World!"}


# path parameter 

#inside main.py
@app.get('/greet/{username}')
async def greet(username:str):
   return {"message":f"Hello {username}"}

# Query parameter search 

user_list = [
   "Shahadat",
   "Masud",
   "Sagor"
] 

@app.get('/search')
async def search_for_user(username:str):
   for user in user_list:
    if username in user_list :
        return {"message":f"details for user {username}"}

    else:
        return {"message":"User Not Found"}


# optional parameter


@app.get('/greet/')
async def greet(username:Optional[str]="User"):
   return {"message":f"Hello {username}"}