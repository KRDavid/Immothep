import pickle
import pandas as pd



# Load from file
with open("./model/model.pkl", 'rb') as file:
    regressor = pickle.load(file)
    
def prediction(prix_moyen: int, surface_t: int, surface_b: int, nb_pieces: int):
    data = [prix_moyen, surface_t, surface_b, nb_pieces]
    Xtest = pd.DataFrame(data, columns=['Prix moyen m²', 'Surface totale terrain', 'Surface totale bati', 'Nombre de pièces'])
    Ypredict = regressor.predict(Xtest)
    return Ypredict
    