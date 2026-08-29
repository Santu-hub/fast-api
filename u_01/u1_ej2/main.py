from fastapi import FastAPI

app = FastAPI()

@app.get("/items/me")
async def read_user_me():
    return {"user": "current"}

@app.get("/items/{item_id}")
async def read_item(user_id:int):
    return {"item_id": user_id}