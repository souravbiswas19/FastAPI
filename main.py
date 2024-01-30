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
def get_posts(new_post: Post):
    print(new_post.title)
    print(new_post.content)
    print(new_post.published)
    print(new_post.rating)
    print(new_post)
    print(new_post.model_dump())
    return {"data":"new post"}
    #return {"new_post": f'title - {payload['title']} content - {payload['content']}'}