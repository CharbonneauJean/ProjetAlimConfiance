import unidecode

def normalisation_nom_ville(nom_ville: str) -> str:
    nom_ville_norm = unidecode.unidecode(nom_ville.lower()).replace('-', ' ').replace('\'', ' ')
    return nom_ville_norm

