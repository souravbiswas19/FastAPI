from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"Data": "This is your post"}

@app.post("/createposts")
def get_posts(new_post: Post):
    print(new_post)
    return {"data":"new post"}
    #return {"new_post": f'title - {payload['title']} content - {payload['content']}'}