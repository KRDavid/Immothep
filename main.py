from typing import Optional

from fastapi import FastAPI

app = FastAPI()


dic = {0: "Chocolat", 1: "Mcdo", 2: "BK", 3: "Gauffres", 4: "gpudidé", 5: "PC", 6: "PS5", 7: "HTC Cosmos", 8: "MOVA", 9: "Saucisson"}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    name = dic[item_id]
    return {"q": q, "item_id": item_id, "item_name": name}