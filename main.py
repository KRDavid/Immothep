from functions import predict
from functions import zip_dictionnary
from typing import Optional
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/estimate/code_po={code_po}&surface_t={surface_t}&surface_b={surface_b}&nb_pieces={nb_pieces}")
def read_item(code_po: int, surface_t: int, surface_b: int, nb_pieces: int):
    prix_moyen = zip_dictionnary.prix_moyen(code_po)
    prix_estime = predict.prediction(prix_moyen, surface_t, surface_b, nb_pieces)
    estimation = prix_estime[0]
    return { "estimation": estimation }