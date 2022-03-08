from mangum import Mangum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World 2"}

@app.get("/test")
async def test_func():
    return {"message": "test message"}

@app.get("/wow")
async def test_func2():
    return {"message": "yeah it's working!"}


handler = Mangum(app=app)