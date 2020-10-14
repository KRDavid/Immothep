"""Permet de sauvegarder le modèle random forest sous fichier json
"""

from sklearn.ensemble import RandomForestRegressor
import numpy as np
import json
import pandas as pd
import os



class RandomForest(RandomForestRegressor):
    """

    Args:
        RandomForestRegressor (obj): Objet de la librairie sklearn.ensemble
    """
    # Override the class constructor
    def __init__(self, n_estimators=10, random_state=1, X_train=None, Y_train=None, data=None):
        """[summary]

        Args:
            n_estimators (int, optional): Nombre d'arbres de décision. 10 par défaut.
            random_state (int, optional): Seed de l'aléatoire. 1 par défaut.
            X_train (df, optional): Données applaties en entrée.
            Y_train (df, optional): Données de sortie.
            data (df, optional): Données non applaties en entrée.
        """
        RandomForestRegressor.__init__(self, n_estimators=n_estimators, random_state=random_state)
        self.X_train = X_train
        self.Y_train = Y_train
        self.data = data
        if not os.path.exists("./model"):
            os.makedirs("./model")

    # Train the model
    def train_model(self):
        """Entrainement du modèle
        """
        RandomForestRegressor.fit(self, self.X_train, self.Y_train)

    # A method for saving object data to JSON file
    def save_json(self, filepath):
        """Sauvegarde du modèle

        Args:
            filepath (str): chemin relatif vers le fichier json
        """
        self.data.to_csv('./model/data.csv')
        dict_ = {}
        dict_['n_estimators'] = self.n_estimators
        dict_['random_state'] = self.random_state
        dict_['X_train'] = self.X_train.tolist() if self.X_train is not None else 'None'
        dict_['Y_train'] = self.Y_train.tolist() if self.Y_train is not None else 'None'

        # Creat json and save to file
        json_txt = json.dumps(dict_, indent=4)
        with open(filepath, 'w') as file:
            file.write(json_txt)

    # A method for loading data from JSON file
    def load_json(self, filepath):
        """Chargement du modèle du modèle

        Args:
            filepath (str): chemin relatif vers le fichier json
        """
        with open(filepath, 'r') as file:
            dict_ = json.load(file)
        self.data = pd.read_csv('./model/data.csv', usecols=['Nombre pieces principales', 'Surface terrain', 'Surface reelle bati', 'Prix moyen m²'])
        self.n_estimators = dict_['n_estimators']
        self.random_state = dict_['random_state']
        self.X_train = np.asarray(dict_['X_train']) if dict_['X_train'] != 'None' else None
        self.Y_train = np.asarray(dict_['Y_train']) if dict_['Y_train'] != 'None' else None