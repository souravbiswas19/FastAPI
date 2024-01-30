from fastapi import FastAPI

app  = FastAPI()

@app.get("/", status_code=200)
def getcar_Info():
    return {"message":"server is running"}