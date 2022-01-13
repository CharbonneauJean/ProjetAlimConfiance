import pandas as pd
import numpy as np

inspections = pd.read_csv('export_alimconfiance.csv', header=0, sep=';', dtype= {3: np.str}, parse_dates = True)

inspections.info()

inspections.sort_values(by = 'SIRET', inplace = True)

# print(inspections.head(10))

for row in inspections.itertuples():
    APP_Libelle_etablissement = row[1]
    SIRET = row[2]
    Adresse_2_UA = row[3]
    Code_postal = row[4]
    Libelle_commune = row[5]
    Numero_inspection = row[6]
    Date_inspection = row[7]
    APP_Libelle_activite_etablissement = row[8]
    Synthese_eval_sanit = row[9]
    Agrement = row[10]
    geores = row[11]
    filtre = row[12]
    ods_type_activite = row[13]

    

