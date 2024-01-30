from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"Data": "This is your post"}

@app.post("/createposts")
def get_posts(post: Post):
    print(post.model_dump())
    return {"data":post}
    #return {"new_post": f'title - {payload['title']} content - {payload['content']}'}