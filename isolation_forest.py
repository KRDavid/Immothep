#coding:utf-8

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest


df = pd.read_csv('salary_test.csv')


model = IsolationForest(n_estimators = 100, max_samples = 'auto', contamination = 'auto', max_features = 1)
model.fit(df[['salary']])


df['scores'] = model.decision_function(df[['salary']])
df['anomaly'] = model.predict(df[['salary']])
print(df.head(10))


anomaly=df.loc[df['anomaly'] == -1]
anomaly_index = list(anomaly.index)
print(anomaly)