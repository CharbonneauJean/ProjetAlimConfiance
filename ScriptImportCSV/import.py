import pandas as pd
import utils
import model

inspections = pd.read_csv('export_alimconfiance.csv', header=0, sep=';', dtype={3: str}, parse_dates=True)

inspections.info()

inspections.sort_values(by='SIRET', inplace=True)

inspections.insert(2, "SIREN", inspections['SIRET'].apply(lambda x: str(x)[:9]), allow_duplicates=True)

inspections.insert(4, "DEPARTEMENT", inspections['Code_postal'].apply(lambda x: str(x)[:2]), allow_duplicates=True)

inspections.insert(7, "COMMUNE_NORM", inspections['Libelle_commune'].apply(lambda x: utils.normalisation_nom_ville(x)),
                   allow_duplicates=True)

inspections['Date_inspection'] = inspections['Date_inspection'].apply(lambda x: str(x)[:10])

inspections.reset_index(inplace=True, drop=True)

print(inspections.head(10))

# etablissement1 = model.Etablissement(
#         siret="000000",
#         siren="123132",
#         libelle_etablissement="Libellé",
#         adresse="Adresse",
#         code_postal="CP45",
#         departement="01",
#         commune="Strasbourg",
#         geores="48.02132132;5.20221",
#         nb_agrements=0,
#         commune_norm="strasbourg")

# model.session.add(etablissement1)  
# model.session.commit()

# for row in inspections.itertuples():
#     APP_Libelle_etablissement = row[1]
#     SIRET = row[2]
#     Adresse_2_UA = row[3]
#     Code_postal = row[4]
#     Libelle_commune = row[5]
#     Numero_inspection = row[6]
#     Date_inspection = row[7]
#     APP_Libelle_activite_etablissement = row[8]
#     Synthese_eval_sanit = row[9]
#     Agrement = row[10]
#     geores = row[11]
#     filtre = row[12]
#     ods_type_activite = row[13]

    # Bosser sur les champs


