from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"Data": "This is your post"}

@app.post("/createposts")
def get_posts(payload: dict=Body(...)):
    return {"new_post": f'title - {payload['title']} content - {payload['content']}'}