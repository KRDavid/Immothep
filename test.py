cleaned_dataframe = pd.read_csv('./data/CURATED/csv_clean_1.csv')

sample_cleaned_dataframe = cleaned_dataframe.sample(n = 10000, random_state = 1)

sample_cleaned_dataframe.to_csv('./data/SAMPLE/sample_1.csv')

df_anomaly = pd.read_csv('./data/CURATED/anomaly_csv_clean_1.csv', sep = ',', decimal = ',')

df_csv_clean = pd.read_csv('./data/CURATED/csv_clean_1.csv', sep = ',', decimal = ',')

df_anomaly = df_anomaly.drop(columns = ['Unnamed: 0'])

df_anomaly = df_anomaly.drop(columns = ['Valeur fonciere', 'Code postal', 'Nombre de lots', 'Nombre pieces principales', 'Surface terrain', 'Surface reelle bati', 'Surface Carrez totale', 'scores'])

df_anomaly = df_anomaly.rename(columns = {'Unnamed: 0.1':'Unnamed: 0'})

df_add_anomaly = df_csv_clean.merge(df_anomaly, how = 'left', on = 'Unnamed: 0')

df_add_anomaly = df_add_anomaly.fillna(0)
