from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/blog")
def index(limit,published:bool,sort:Optional[str]=None):
    # return published
    if published:
        return {"data":f'{limit} published blogs from the db'}
    return "no data published"


@app.get("/blog/{id}/comments")
def comments(id):
    return {'data':{'1','2'}}

@app.get("/blog/unpublished")
def unpublished():
    return {"data":"unpublished data"}

@app.get("/blog/{id}")
def show(id:int):
    return {'data':id}


class Blog(BaseModel):
    title:str
    body:str
    published_at:Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    # return request
    return {"data":f"blog is created with {request.title}"}
