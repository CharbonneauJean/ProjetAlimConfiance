import pandas as pd
import numpy as np
import utils

inspections = pd.read_csv('export_alimconfiance.csv', header=0, sep=';', dtype={3: str}, parse_dates=True)

# on enlève la colonne filtre inutile
inspections.drop(['filtre'], axis=1, inplace=True)

# on tri le dataset par SIRET afin de détecter plus facilement les mêmes établissements
inspections.sort_values(by='SIRET', inplace=True)

# on enlève les observations qui ont un geores ou un code postal vide
inspections = inspections.dropna(subset=['geores', 'Code_postal'])

# on ajoute la colonne SIREN qui sera utilse pour identifier les établissements appartenant au même groupe
inspections.insert(2, "SIREN", inspections['SIRET'].apply(lambda x: str(x)[:9]), allow_duplicates=True)

# on ajoute la colonne DEPARTEMENT afin d'avoir une localisation départementale
inspections.insert(4, "DEPARTEMENT", inspections['Code_postal'].apply(lambda x: int(str(x)[:2])), allow_duplicates=True)
 
# on ne garde que les inspections françaises
inspections = inspections.drop(inspections[inspections.DEPARTEMENT > 95].index)

# on normalise les noms de ville pour pouvoir plus facilement les standardiser par la suite
inspections.insert(7, "COMMUNE_NORM", inspections['Libelle_commune'].apply(lambda x: utils.normalisation_nom_ville(x)),
                   allow_duplicates=True)

# on ne prend que la partie date qui nous intéresse sans l'heure
inspections['Date_inspection'] = inspections['Date_inspection'].apply(lambda x: str(x)[:10])

# on récupère la latitude et la longitude séparément
inspections.insert(14, "GEORES_LAT", inspections['geores'].apply(lambda x: str(x).split(',')[0]),
                   allow_duplicates=True)

inspections.insert(15, "GEORES_LON", inspections['geores'].apply(lambda x: str(x).split(',')[1]),
                   allow_duplicates=True)

# on remplace les NA par des chaines vides
inspections[['Agrement', 'Adresse_2_UA']] = inspections[['Agrement', 'Adresse_2_UA']].fillna('')

# on remplace les libellés marqués par un "_" par des chaines vides

# inspections['APP_Libelle_activite_etablissement'] = inspections['APP_Libelle_activite_etablissement'].str.replace('_',np.nan)

inspections["APP_Libelle_activite_etablissement"].replace({"_": np.nan}, inplace=True)

# on drop les lignes qui ont un libelle vide
inspections = inspections.dropna(subset=['APP_Libelle_activite_etablissement'])

# on drop les lignes qui ont un SIRET malformé
inspections = inspections[inspections["SIRET"].str.isdecimal() == True]

# on remplace les ; par des virgules dans le nom de l'établissement

inspections['APP_Libelle_etablissement'] = inspections['APP_Libelle_etablissement'].str.replace(';',',')

# inspections["APP_Libelle_etablissement"].replace({";": ","}, inplace=True)

# on remplace les ; par des virgules dans l'adresse
inspections['Adresse_2_UA'] = inspections['Adresse_2_UA'].str.replace(';',',')

#inspections["Adresse_2_UA"].replace({";": ","}, inplace=True)


# on réinitialise l'index
inspections.reset_index(inplace=True, drop=True)

# on exporte le CSV clean qui servira pour l'import en BDD.
inspections.to_csv('export_alimconfiance_clean.csv', sep=';')





