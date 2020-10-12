

from typing import Optional

from fastapi import FastAPI

app = FastAPI()


dic = {0: "Chocolat", 1: "Mcdo", 2: "BK", 3: "Gauffres", 4: "gpudidé", 5: "PC", 6: "PS5", 7: "HTC Cosmos", 8: "MOVA", 9: "Saucisson"}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/estimate/{code_po},{surface_t},{surface_b},{nb_pieces}")
def read_item(code_po: int, surface_t: int, surface_b: int, nb_pieces: int):

    return {"estimation" : 0}