from functions.randomforestclass import RandomForest
import pandas as pd
from sklearn.preprocessing import StandardScaler



# Create a new object and load its data from JSON file
json_randomforest = RandomForest()  
json_randomforest.load_json("./model/model.json")
json_randomforest.train_model() 
    
def prediction(prix_moyen: int, surface_t: int, surface_b: int, nb_pieces: int):
    data = {"prix moyen": [prix_moyen], "surface terrain": [surface_t], "surface bati": [surface_b], "nb pieces": [nb_pieces]}
    X_test = pd.DataFrame(data)
    print(X_test)
    sc = StandardScaler()
    X_test = sc.fit_transform(X_test)
    print(X_test)
    Ypredict = json_randomforest.predict(X_test)
    return Ypredict
    