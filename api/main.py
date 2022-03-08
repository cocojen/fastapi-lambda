from mangum import Mangum
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World 2"}

@app.get("/test")
async def test_func():
    return {"message": "test message"}



handler = Mangum(app=app)