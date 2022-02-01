
import pandas as pd
import utils
import model

inspections = pd.read_csv('export_alimconfiance_clean.csv', header=0, sep=';', dtype={2 :str, 3: str, 6 : str}, parse_dates=True)

inspections.info()

    # Liste des colonnes récupérées, pour info
    #
    # lineIndex = row[1]
    # APP_Libelle_etablissement = row[2]
    # SIRET = row[3]
    # SIREN = row[4]
    # Adresse_2_UA = row[5]
    # DEPARTEMENT = row[6]
    # Code_postal = row[7]
    # Libelle_commune = row[8]
    # COMMUNE_NORM = row[9]
    # Numero_inspection = row[10]
    # Date_inspection = row[11]
    # APP_Libelle_activite_etablissement = row[12]
    # Synthese_eval_sanit = row[13]
    # Agrement = row[14]
    # geores = row[15]
    # GEORES_LAT = row[16]
    # GEORES_LON = row[17]
    # ods_type_activite = row[18]

inspections.sample(1)

inspections['Synthese_eval_sanit'].value_counts()

inserted_activite = {}

def addUniqueActivite(libelle_activite, categorie_frais):
    if(libelle_activite not in list(inserted_activite.values())):
        activite = model.Activite(libelle_activite = libelle_activite, categorie_frais = categorie_frais)
        model.session.add(activite)
        model.session.commit()
        model.session.refresh(activite)
        inserted_activite[activite.idactivite] = activite.libelle_activite

def addMultipleActivite(libelle_activite_multiple : str):
    strArr = libelle_activite_multiple.split('|')
    for libelle_activite in strArr:
        addUniqueActivite(libelle_activite, False)

# Ajout des activités dans la table activité
for row in inspections.itertuples():
    APP_Libelle_activite_etablissement = row[12]
    ods_type_activite = row[18]

    if(ods_type_activite == 'Autres'):
        if('|' in APP_Libelle_activite_etablissement):
            # print("Multi activity detected", APP_Libelle_activite_etablissement)
            addMultipleActivite(APP_Libelle_activite_etablissement)
        else:
            # print('Single activity detected')
            addUniqueActivite(APP_Libelle_activite_etablissement, False)
    else:
        # print('FRESH activity detected')
        addUniqueActivite(APP_Libelle_activite_etablissement + "," + ods_type_activite, True)       


inserted_etablissement = {}

def addUniqueEtablissement(
        libelle_etablissement,
        siret,
        siren,
        adresse,
        departement,
        code_postal,
        commune,
        commune_norm,
        geores,
        geores_lat,
        geores_lon):
    uniqueEtabHash = libelle_etablissement.strip().lower() + siret.strip() + commune_norm.strip()

    if(uniqueEtabHash not in list(inserted_etablissement.keys())):
        etablissement = model.Etablissement(
            libelle_etablissement = libelle_etablissement,
            siret = siret,
            siren = siren,
            adresse = adresse,
            departement = departement,
            code_postal = code_postal,
            commune = commune,
            commune_norm = commune_norm,
            geores = geores,
            geores_lat = geores_lat,
            geores_lon = geores_lon
        )
        model.session.add(etablissement)
        model.session.commit()
        model.session.refresh(etablissement)
        inserted_etablissement[uniqueEtabHash] = etablissement.idetablissement

# Ajout des établissements dans la table etablissement
for row in inspections.itertuples():
    APP_Libelle_etablissement = row[2]
    SIRET = row[3]
    SIREN = row[4]
    Adresse_2_UA = row[5]
    DEPARTEMENT = row[6]
    Code_postal = row[7]
    Libelle_commune = row[8]
    COMMUNE_NORM = row[9]
    geores = row[15]
    GEORES_LAT = row[16]
    GEORES_LON = row[17]

    addUniqueEtablissement(
        APP_Libelle_etablissement,
        SIRET,
        SIREN,
        Adresse_2_UA,
        DEPARTEMENT,
        Code_postal,
        Libelle_commune,
        COMMUNE_NORM,
        geores,
        GEORES_LAT,
        GEORES_LON
    )

inserted_inspections = {}

def addUniqueInspection(numero_inspection, date_inspection, synthese_eval, numero_agrement, idetablissement, idactivite):
    uniqueInspectionHash = numero_inspection.strip() + ',' + str(idetablissement) + ',' + str(idactivite) + str(date_inspection)

    if(uniqueInspectionHash not in list(inserted_inspections.keys())):
        inspection = model.Inspection(
            numero_inspection = numero_inspection,
            date_inspection = date_inspection,
            synthese_eval = synthese_eval,
            numero_agrement = numero_agrement,
            idetablissement = idetablissement,
            idactivite = idactivite
        )

        model.session.add(inspection)
        model.session.commit()
        model.session.refresh(inspection)
        inserted_inspections[uniqueInspectionHash] = inspection.idinspection

# Ajout des inspections dans la table inspection
for row in inspections.itertuples():
    APP_Libelle_etablissement = row[2]
    SIRET = row[3]
    COMMUNE_NORM = row[9]
    Numero_inspection = row[10]
    Date_inspection = row[11]
    APP_Libelle_activite_etablissement = row[12]
    Synthese_eval_sanit = row[13]
    Agrement = row[14]
    ods_type_activite = row[18]

    uniqueEtabHash = APP_Libelle_etablissement.strip().lower() + SIRET.strip() + COMMUNE_NORM.strip()
    thisIdEtablissement = inserted_etablissement.get(uniqueEtabHash)

    if(ods_type_activite == 'Autres'):
        if('|' in APP_Libelle_activite_etablissement):
            # Multi inspection detected
                strArr = APP_Libelle_activite_etablissement.split('|')
                for libelle_activite in strArr:
                    thisIdActivite = utils.get_key(libelle_activite, inserted_activite)
                    addUniqueInspection(Numero_inspection, Date_inspection, Synthese_eval_sanit, Agrement, thisIdEtablissement, thisIdActivite)
        else:
            # Single inspection detected
            thisIdActivite = utils.get_key(APP_Libelle_activite_etablissement, inserted_activite)
            addUniqueInspection(Numero_inspection, Date_inspection, Synthese_eval_sanit, Agrement, thisIdEtablissement, thisIdActivite)
    else:
        # Single FRESH inspection detected
        thisIdActivite = utils.get_key(APP_Libelle_activite_etablissement + "," + ods_type_activite, inserted_activite)
        addUniqueInspection(Numero_inspection, Date_inspection, Synthese_eval_sanit, Agrement, thisIdEtablissement, thisIdActivite)

    

# On clean la colonne numero_agrement des valeur NaN
model.session.execute("update inspection set numero_agrement = null where numero_agrement = 'NaN'")
model.session.commit()

score_tres_satisfaisant = 4
score_satisfaisant = 3
score_a_ameliorer = 2
score_a_corriger_d_urgence = 1

sum_scores = 0
nb_scores = 0

stmt = model.session.execute("select inspection.idetablissement, count(inspection.idinspection) as nbInspections from inspection group by inspection.idetablissement order by nbInspections desc")
for row in stmt:
    # on va calculer le score moyen
    thisIdEtablissement = row[0]
    stmt_1 = model.session.execute(f"select synthese_eval from inspection where idetablissement = {thisIdEtablissement} order by date_inspection")
    for row_1 in stmt_1:
        if(row_1[0] == "Très satisfaisant"):
            sum_scores += score_tres_satisfaisant
        elif(row_1[0] == "Satisfaisant"):
            sum_scores += score_satisfaisant
        elif(row_1[0] == "A améliorer"):
            sum_scores += score_a_ameliorer
        else:
            sum_scores += score_a_corriger_d_urgence
        nb_scores+=1
    thisMoyScore = sum_scores/nb_scores
    # print('Avg score for etablissement id ', thisIdEtablissement, ' : ', str(thisMoyScore))
    model.session.execute(f"UPDATE etablissement set moy_score={thisMoyScore}, nb_inspections={row[1]} where idetablissement={thisIdEtablissement}")
    model.session.commit()
    sum_scores=0
    nb_scores=0


stmt = model.session.execute("select idetablissement, count(distinct numero_agrement) as nbAgrements from inspection where numero_agrement is not null group by idetablissement order by nbAgrements desc")

for row in stmt:
    # on met à jour le nombre d'agréments pour chaque établissement
    model.session.execute(f"UPDATE etablissement set nb_agrements={row[1]} where idetablissement={row[0]}")
    model.session.commit()

stmt = model.session.execute("UPDATE etablissement set nb_agrements=0 where nb_agrements is null")
model.session.commit()




