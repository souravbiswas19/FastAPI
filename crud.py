from fastapi import FastAPI
from pydantic import BaseModel

app  = FastAPI()

class Person(BaseModel):
    id: int
    firstname: str
    lastname:str
    ismale: bool


@app.get("/", status_code=200)
def getPerson_Info():
    return {"message":"server is running"}

@app.get('/getpersonbyid/{person_id}', status_code=200)
def getPerson_by_Id(person_id: int):
    return {"message": f'Your person id is {person_id}'}

@app.post('/addpersoninfo', status_code=200)
def addPerson_Info(person:Person):
    return {
        'id': person.id,
        'firstname':person.firstname,
        'lastname':person.lastname,
        'isMale':person.ismale
        }