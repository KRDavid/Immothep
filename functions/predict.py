from functions.randomforestclass import RandomForest
import pandas as pd
from sklearn.preprocessing import StandardScaler



# Create a new object and load its data from JSON file
json_randomforest_maison = RandomForest()  
json_randomforest_maison.load_json("./model/model_maison.json", './model/data_maison.csv')
json_randomforest_maison.train_model()
sc = StandardScaler()
sc.fit_transform(json_randomforest_maison.data)

json_randomforest_appart = RandomForest()  
json_randomforest_appart.load_json("./model/model_appart.json", './model/data_appart.csv')
json_randomforest_appart.train_model()


    
def prediction_maison(prix_moyen: float, surface_t: int, surface_b: int, nb_pieces: int):
    data = {"nb pieces": [nb_pieces], "surface terrain": [surface_t], "surface bati": [surface_b], "prix moyen": [prix_moyen]}
    X_test = pd.DataFrame(data)
    X_test = sc.transform(X_test)
    Ypredict = json_randomforest_maison.predict(X_test)
    return Ypredict

def prediction_appart(prix_moyen: float, surface_t: int, surface_b: int, nb_pieces: int):
    data = {"nb pieces": [nb_pieces], "surface terrain": [surface_t], "surface bati": [surface_b], "prix moyen": [prix_moyen]}
    X_test = pd.DataFrame(data)
    X_test = sc.transform(X_test)
    Ypredict = json_randomforest_appart.predict(X_test)
    return Ypredict