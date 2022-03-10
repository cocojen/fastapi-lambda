from mangum import Mangum
from fastapi import FastAPI
import numpy as np

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World 2"}

@app.get("/test")
async def test_func():
    return {"message": "test message"}


@app.get("/numpy")
async def test_package_numpy():
    a = np.arange(15).reshape(3, 5)
    return {"message": a.ndim}


handler = Mangum(app=app)