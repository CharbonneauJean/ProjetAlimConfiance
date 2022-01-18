# Pandas


## Importer pandas et récupérer un fichier tsv
```python
import pandas as pd

food = pd.read_csv('C:/Users/jeanc/Downloads/archive/en.openfoodfacts.org.products.tsv', sep='\t', header=0)
```


## Taille de la DataFrame
```python
len(dataFrame) 
```

