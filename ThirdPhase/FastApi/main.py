from fastapi import FastAPI
from model import Item
app = FastAPI()

@app.get("/")
def read_root():
    return{"message":"Hello World"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return{"user_id": user_id, "name": "Username"}

@app.get("/items")
def get_items():
    return[{"id":1, "name": "Item 1"} , {"id": 2, "name": "item 2"}]

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item{item_id}"}

@app.get("/search")
def search(q:str, skip: int=0, limit: int = 100):
    return {"query": q, "skip": skip, "limit": limit}


@app.post("/items")
def create_item(item:Item):
    return {"created": True, "item": item}

@app.put("/items/item_id")
def update_item(item_id : int, item: Item):
    return {"item_id":item_id, "updated" : True, "item": item}

@app.delete("/items/item_id")
def delete_item(item_id:int):
    return {"deleted": True, "item_id": item_id}