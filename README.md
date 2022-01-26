# Title

# Procédure d'installation

# Installer Anaconda

# Créer un environnement python 3.9 - nom : ProjetAlimConfiance

# ouvrir Cmd.exe à travers Anaconda Navigator

# Installer les dépendances

```
pip install pandas sqlalchemy unidecode
conda install psycopg2
pip install sqlacodegen
```

# Pour générer les classes python correspondantes aux tables SQL

```
sqlacodegen "postgresql://postgres:root@localhost:5432/AlimConfiance"
```

