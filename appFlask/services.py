import model
import dtos
from joblib import load
import os
import pandas as pd

def getModelResult(modelName : str, itemInspection : dtos.SearchItem):
    fileName = modelName + '_model.data'
    if(os.path.exists(fileName)):
        thisModel = load(modelName + '_model.data')

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
                where idinspection = {itemInspection.idinspection}
            """)

        for row in stmt:
            commune_norm = row['commune_norm']
            geores_lat = row['geores_lat']
            geores_lon = row['geores_lon']
            siren = row['siren']
            categorie_frais = row['categorie_frais']
            nb_agrements = row['nb_agrements']
            nb_inspections = row['nb_inspections']
            departement = row['departement']
            idactivite = row['idactivite']

        # data = [['commune_norm', commune_norm],
        #  ['geores_lat', geores_lat],
        #  ['geores_lon', geores_lon],
        #  ['siren', siren],
        #  ['categorie_frais', categorie_frais],
        #  ['nb_agrements', nb_agrements],
        #  ['nb_inspections', nb_inspections],
        #  ['departement', departement],
        #  ['idactivite', idactivite]]

        data = [
            ['commune_norm', 'geores_lat','geores_lon','siren','categorie_frais', 'nb_agrements', 'nb_inspections', 'departement','idactivite' ],
            [commune_norm, geores_lat, geores_lon, siren, categorie_frais, nb_agrements, nb_inspections, departement, idactivite]
            ]

        # Create the pandas DataFrame
        df = pd.DataFrame(data, columns = ['commune_norm','geores_lat','geores_lon','siren','categorie_frais','nb_agrements','nb_inspections','departement','idactivite'])

        print("#############################")
        print(thisModel.predict(df))
    else:
        return 3


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
    resultJean = 2 # getModelResult('jean', item1)

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


