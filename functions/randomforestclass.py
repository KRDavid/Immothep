from sklearn.ensemble import RandomForestRegressor
import numpy as np
import json


class RandomForest(RandomForestRegressor):

    # Override the class constructor
    def __init__(self, n_estimators=10, random_state=1, X_train=None, Y_train=None):
        RandomForestRegressor.__init__(self, n_estimators=n_estimators, random_state=random_state)
        self.X_train = X_train
        self.Y_train = Y_train

    # Train the model
    def train_model(self):
        RandomForestRegressor.fit(self, self.X_train, self.Y_train)

    # A method for saving object data to JSON file
    def save_json(self, filepath):
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
        with open(filepath, 'r') as file:
            dict_ = json.load(file)

        self.n_estimators = dict_['n_estimators']
        self.random_state = dict_['random_state']
        self.X_train = np.asarray(dict_['X_train']) if dict_['X_train'] != 'None' else None
        self.Y_train = np.asarray(dict_['Y_train']) if dict_['Y_train'] != 'None' else None