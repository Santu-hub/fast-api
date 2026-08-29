from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Monitor"},
    {"item_name": "Teclado"},
    {"item_name": "Mouse"},
]

@app.get("/items/")
async def read_items(skip: int=0, limit: int=10):
    return fake_items_db[skip : skip+limit]

@app.get("/items/{item_id}")
async def read_item(item_id:str, q:str | None = None):
    if q:
        return{"item_id": item_id, "q": q}
    return {"item_id":item_id}

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q:str | None = None,
    short: bool = False,
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item["q"] = q
    if not short:
        item["descripcion"] = "descripcion larga del item"
    return item

@app.get("/items1/{item_id}")
async def read_user_item(item_id: str, needy:str):
    item = {"item_id": item_id, "needy": needy}
    return item