from fastapi import FastAPI

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


