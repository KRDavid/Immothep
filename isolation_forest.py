#coding:utf-8

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest


df = pd.read_csv('./data/CURATED/csv_clean_bordeaux.csv')


model = IsolationForest(n_estimators = 100, max_samples = 'auto', contamination = 'auto', max_features = 1)
model.fit(df[['Valeur fonciere', 'Nombre pieces principales', 'Surface terrain', 'Surface reelle bati']])


df['scores'] = model.decision_function(df[['Valeur fonciere', 'Nombre pieces principales', 'Surface terrain', 'Surface reelle bati']])
df['anomaly'] = model.predict(df[['Valeur fonciere', 'Nombre pieces principales', 'Surface terrain', 'Surface reelle bati']])
print(df.head(10))


anomaly=df.loc[df['anomaly'] == -1]
anomaly_index = list(anomaly.index)
print(anomaly)

anomaly.to_csv('./data/CURATED/anomaly_csv_clean_bordeaux.csv')