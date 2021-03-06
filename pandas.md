# Pandas


## Importer pandas et récupérer un fichier tsv
```python
import pandas as pd

df = pd.read_csv('C:/Users/jeanc/Downloads/archive/en.openfoodfacts.org.products.tsv', sep='\t', header=0)
```


## Taille de la DataFrame
```python
len(df) 
```

## Nombre de colonnes de la DataFrame
```python
len(df.columns)
```

## Dimensionnalité du DataFrame
```python
df.shape
df.shape[0] # <- nb lignes
df.shape[1] # <- nb colonnes
```

## Va compter le nombre d'objets non vide (not None, Nan, Nat) par colonne
```python
df.count()
# equivalent à : df.count(axis='rows')
# df.count(axis=0)
```
> /!\ Attention contre-intuitif /!\

## Va compter le nombre d'objets non vide (not None, Nan, Nat) par ligne
```python
df.count(axis='columns')
# df.count(axis=1)
```


## Selectionner les colonnes selon le range précisé
```python
df.columns[:] # toutes les colonnes
df.columns[1:6]
```

## Afficher les colonnes
```python
for colNum, col in enumerate(df.columns):
    print(str(colNum) + ":" + col, end = ' ')
```

## Afficher les colonnes sous forme de list
```python
df.columns.values.tolist()
# list(df.columns)
```

## Affiche la ligne n
```python
df.iloc[n]
```

## Affiche les lignes selon le range précisé
```python
df.iloc[0:104] # les 104 premiers enregistrements
```

## Affiche les lignes demandées dans la list fournie
```python
df.iloc[ [2, 3, 4] ] # on obtient les lignes 2, 3 et 4
```

## Obtenir le type de la colonne donnée
```python
df.dtypes[104] # -> dtype('float64') par exemple
```

## Obtenir la liste des valeurs de cette colonne
```python
df["column_name"]
```

## Obtenir la valeur de cette colonne pour la ligne n
```python
df["column_name"].iloc[n]
```

## Obtenir la valeur précise de la ligne x et de la colonne y
```python
df.values[x][y]
```

## Ajouter une colonne à une DataFrame
```python
# Step 1 : créer la liste des valeurs de la colonne
listValeurs = ['Val1', 'Val2', 'Val3', 'Val4']
# Step 2 : ajouter la colonne
df['newColumnName'] = listValeurs
```

## Ajouter une colonne à une DataFrame à une position précise
```python
# Step 1 : créer la liste des valeurs de la colonne
listValeurs = ['Val1', 'Val2', 'Val3', 'Val4']
# Step 2 : ajouter la colonne
df.insert(position, "newColumnName", listValeurs, allow_duplicates = True)
```

## Prendre seulement certaines colonnes du DataFrame
```python
df[ ["column_name1", "column_name2", "column_name2"] ]
```

## Grouper les lignes selon une colonne
```python
df[ ["column_name1", "column_name2", "column_name2"] ].groupby("column_name1")
```

## Appliquer une fonction d'aggrégation sur le regroupement
```python
df[ ["column_name1", "column_name2", "column_name2"] ].groupby("column_name1").sum("column_name2")
```

## Trier les valeurs selon la colonne précisée (paramètre ascending par défaut à True)
```python
df[ ["column_name1", "column_name2", "column_name2"] ].groupby("column_name1").sum("column_name2").sort_values('quantity', ascending=False)
```

## Appliquer une fonction (lambda) sur toutes les valeurs de la colonne
```python
df['column_name1'] = df['column_name1'].apply(lambda x: float(x.replace("$", " "))) # ici ça remplace le $ par un espace
```

## Retourne les valeurs de la colonne en enlevant les doublons
```python
df['column_name'].unique()
```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```

## Titre
```python

```
