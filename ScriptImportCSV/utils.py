import unidecode
import pandas as pd
import model


def normalisation_nom_ville(nom_ville: str) -> str:
    nom_ville_norm = unidecode.unidecode(nom_ville.lower()).replace('-', ' ').replace('\'', ' ')
    return nom_ville_norm

# function to return key for any value in a dict
def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"


def fillWords(df):

    words = {}

    for row in df.itertuples():
        idinspection = int(row[0])

        stmt = model.session.execute(f"""
            select motcle from mots_cles 
            where 1=1
            and idmotcle in ( select idmotcle from motcle_inspection where idinspection in ( select idinspection from inspection where idinspection = {idinspection} ))
            and char_length(motcle) > 3
            and (motcle ~* '[a-z]') is true
            and motcle not in ('satisfaisant', 'ameliorer', 'corriger', 'maniere', 'urgente', 'tres')
            order by char_length(motcle) desc, motcle desc
            limit 13            """
        )

        iter = 1
        for row1 in stmt:
            if(iter < 10):
                wordName = 'word0' + str(iter)
            else:
                wordName = 'word' + str(iter)
            
            if(wordName not in words.keys()):
                words[wordName] = []
            words[wordName].append(row1[0])

            iter+=1
        
    for key in words.keys():
        df[key] = pd.Series(words[key])

    return df