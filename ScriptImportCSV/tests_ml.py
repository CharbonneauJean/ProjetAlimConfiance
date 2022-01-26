import pandas as pd
import unidecode


def normalisation_nom_ville(nom_ville: str) -> str:
    nom_ville_norm = unidecode.unidecode(nom_ville.lower()).replace('-', ' ').replace('\'', ' ')
    return nom_ville_norm


inspections = pd.read_csv('export_alimconfiance.csv', header=0, sep=';', dtype={3: str}, parse_dates=True)

inspections.info()

inspections.sort_values(by='SIRET', inplace=True)

inspections.insert(2, "SIREN", inspections['SIRET'].apply(lambda x: str(x)[:9]), allow_duplicates=True)

inspections.insert(4, "DEPARTEMENT", inspections['Code_postal'].apply(lambda x: str(x)[:2]), allow_duplicates=True)

inspections.insert(7, "COMMUNE_NORM", inspections['Libelle_commune'].apply(lambda x: normalisation_nom_ville(x)),
                   allow_duplicates=True)

inspections.insert(16, "LIBELLE_CONCAT", inspections['APP_Libelle_activite_etablissement'] + "||" + inspections['filtre'],
                   allow_duplicates=True)


inspections['Date_inspection'] = inspections['Date_inspection'].apply(lambda x: str(x)[:10])

inspections.reset_index(inplace=True, drop=True)

print(inspections.head(10))

import numpy as np 
import matplotlib.pyplot as plt 
import scikitplot as skplt
from sklearn import metrics

# variables dépendantes (features)
X = inspections
# variable indépendante (target) 
y = inspections[""]
# description détaillée du jeu de données. 
print(data.DESCR)