from functions.randomforestclass import RandomForest
import pandas as pd
from sklearn.preprocessing import StandardScaler



# Create a new object and load its data from JSON file
json_randomforest = RandomForest()  
json_randomforest.load_json("./model/model.json")
json_randomforest.train_model()
sc = StandardScaler()
sc.fit_transform(json_randomforest.data)
    
def prediction(prix_moyen: float, surface_t: int, surface_b: int, nb_pieces: int):
    data = {"nb pieces": [nb_pieces], "surface terrain": [surface_t], "surface bati": [surface_b], "prix moyen": [prix_moyen]}
    X_test = pd.DataFrame(data)
    X_test = sc.transform(X_test)
    print(X_test)
    Ypredict = json_randomforest.predict(X_test)
    return Ypredict
    