import unidecode

def normalisation_nom_ville(nom_ville: str) -> str:
    nom_ville_norm = unidecode.unidecode(nom_ville.lower()).replace('-', ' ').replace('\'', ' ')
    return nom_ville_norm

# function to return key for any value in a dict
def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"