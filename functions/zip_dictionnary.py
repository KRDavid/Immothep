import pandas as pd

def prix_moyen(code_po):
    df_clean2 = pd.read_csv('./data/CURATED/csv_clean_2.csv', usecols=['Valeur fonciere', 'Code postal', 'Surface reelle bati'])
    df_clean2["Prix moyen m²"] = df_clean2['Valeur fonciere']/df_clean2['Surface reelle bati']
    df_prix_moyen = df_clean2.groupby('Code postal').mean('Prix moyen m²').drop(columns=['Valeur fonciere', 'Surface reelle bati'])

    dict_prix_moyen = df_prix_moyen.to_dict()
    prix_moy = dict_prix_moyen['Prix moyen m²'][code_po]

    return prix_moy