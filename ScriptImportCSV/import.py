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

inspections['Date_inspection'] = inspections['Date_inspection'].apply(lambda x: str(x)[:10])

print(inspections.head(10))

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

    # Bosser sur les champs

inspections.to_csv('out.csv', sep=';')
