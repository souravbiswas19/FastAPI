from fastapi import FastAPI

app  = FastAPI()

class Person:
    id: int
    firstname: str
    lastname:str
    ismale: bool


@app.get("/", status_code=200)
def getPerson_Info():
    return {"message":"server is running"}