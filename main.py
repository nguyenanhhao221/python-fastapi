from typing import Union

import uvicorn
from fastapi import FastAPI

# Initialize fast api
app = FastAPI()


@app.get("/health")
async def check_health():
    return {"status": "alive"}


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
