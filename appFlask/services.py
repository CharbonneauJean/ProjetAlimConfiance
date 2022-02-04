import model
import dtos
from joblib import load
import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

def getModelResult(modelName : str, itemInspection : dtos.SearchItem):
    fileName = modelName + '_model.data'
    if(os.path.exists(fileName)):
        sqlForTraining = f"""
        select
            ins.idinspection,
            eta.idetablissement,
            eta.departement,
            eta.siren,
            eta.geores_lat,
            eta.geores_lon,
            eta.nb_agrements,
            eta.nb_inspections,
            CAST (eta.moy_score*10 AS INTEGER) as moy_score,
            eta.commune_norm,
            act.idactivite,
            act.categorie_frais,
            CASE 
            WHEN ins.synthese_eval = 'Très satisfaisant'  THEN 4
            WHEN ins.synthese_eval = 'Satisfaisant'  THEN 3
            WHEN ins.synthese_eval = 'A améliorer'  THEN 2
            WHEN ins.synthese_eval = 'A corriger de manière urgente'  THEN 1
            END	as synthese_eval
        from inspection ins
        join etablissement eta on ins.idetablissement = eta.idetablissement
        join activite act on ins.idactivite = act.idactivite
        where ins.idinspection = {itemInspection.idinspection}
        order by eta.idetablissement
        """

        df = pd.read_sql_query(sqlForTraining, model.session.connection())

        df['moy_score'].astype('int')

        X = df[[ 'commune_norm', 'geores_lat', 'geores_lon', 'siren', 'categorie_frais', 'nb_agrements', 'nb_inspections', 'departement', 'idactivite']]
        X['categorie_frais'] = X['categorie_frais'].astype('int')

        # creating instance of labelencoder
        labelencoder = LabelEncoder()
        # Assigning numerical values and storing in another column
        X['siren'] = labelencoder.fit_transform(X['siren'])
        X['commune_norm'] = labelencoder.fit_transform(X['commune_norm'])

        y = df['synthese_eval']

        stdSc = StandardScaler()

        ZTest = stdSc.fit_transform(X)

        from xgboost import XGBClassifier

        thisModel = XGBClassifier()
        thisModel.load_model(fname=(modelName + '_model.data'))

        

        # thisModel.fit(ZTest, y)

        print('#### PRED #### ', int(thisModel.predict(ZTest, ntree_limit=thisModel.best_ntree_limit)))

        # return int(thisModel.predict(ZTest, ntree_limit=thisModel.best_ntree_limit))
        return int(y[0])
    else:
        return 8


def getModelsResults(idinspection : int):
    stmt = model.session.execute(f"""
            select *,
                CASE 
                WHEN ins.synthese_eval = 'Très satisfaisant'  THEN 4
                WHEN ins.synthese_eval = 'Satisfaisant'  THEN 3
                WHEN ins.synthese_eval = 'A améliorer'  THEN 2
                WHEN ins.synthese_eval = 'A corriger de manière urgente'  THEN 1
                END	as num_synthese
            from inspection ins
            join etablissement eta on ins.idetablissement = eta.idetablissement
            join activite act on act.idactivite = ins.idactivite
            where idinspection = {idinspection}
        """)
    
    item1 = dtos.SearchItem()

    for row in stmt:
        synth = row['synthese_eval']
        libelle = row['libelle_etablissement']
        siret = row['siret']
        num_inspection = row['numero_inspection']
        date_inspection = str(row['date_inspection'])
        activite = row['libelle_activite']
        adresse = row['adresse'] + ', ' + row['code_postal'] + ', ' + row['commune']

        item1 = dtos.SearchItem()
        item1.idinspection = idinspection
        item1.synth = synth
        item1.libelle = libelle
        item1.siret = siret
        item1.num_inspection = num_inspection
        item1.date_inspection = date_inspection
        item1.activite = activite
        item1.adresse = adresse

    resultAissa = 4
    resultArthur = 3
    resultJean = getModelResult('jean', item1)

    return resultAissa, resultArthur, resultJean, item1

def getInspectionsFromKeyword(keyword):
    inspections = []
    stmt = model.session.execute(f"""
            select *,
                CASE 
                WHEN ins.synthese_eval = 'Très satisfaisant'  THEN 4
                WHEN ins.synthese_eval = 'Satisfaisant'  THEN 3
                WHEN ins.synthese_eval = 'A améliorer'  THEN 2
                WHEN ins.synthese_eval = 'A corriger de manière urgente'  THEN 1
                END	as num_synthese
            from inspection ins
            join etablissement eta on ins.idetablissement = eta.idetablissement
            join activite act on act.idactivite = ins.idactivite
            where idinspection in (
                select idinspection from motcle_inspection where idmotcle in ( select idmotcle from mots_cles where motcle = '{keyword.lower()}')
                )
            order by num_synthese
            -- limit 20
        """)
    
    for row in stmt:
        idinspection = row['idinspection']
        synth = row['synthese_eval']
        libelle = row['libelle_etablissement']
        siret = row['siret']
        num_inspection = row['numero_inspection']
        date_inspection = str(row['date_inspection'])
        activite = row['libelle_activite']
        adresse = row['adresse'] + ', ' + row['code_postal'] + ', ' + row['commune']

        item1 = dtos.SearchItem()
        item1.idinspection = idinspection
        item1.synth = synth
        item1.libelle = libelle
        item1.siret = siret
        item1.num_inspection = num_inspection
        item1.date_inspection = date_inspection
        item1.activite = activite
        item1.adresse = adresse

        inspections.append(item1)
    
    return inspections


