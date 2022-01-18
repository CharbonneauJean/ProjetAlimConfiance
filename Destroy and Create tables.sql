/* CREATE DATABASE "AlimConfiance" WITH OWNER = postgres ENCODING = 'UTF8'; */

DROP TABLE IF EXISTS INSPECTION;
DROP TABLE IF EXISTS ETABLISSEMENT;
DROP TABLE IF EXISTS ACTIVITE;

CREATE TABLE IF NOT EXISTS ETABLISSEMENT(
   IDETABLISSEMENT SERIAL,
   SIRET VARCHAR(200),
   SIREN VARCHAR(200),
   NIC VARCHAR(200),
   LIBELLE_ETA VARCHAR(200),
   ADRESSE VARCHAR(200),
   CODE_POSTAL VARCHAR(200),
   DEPARTEMENT VARCHAR(200),
   COMMUNE VARCHAR(200), -- "Vézelay-En-Truc" "Vézelay En Truc" "VEZELAY EN TRUC"
   COMMUNE_NORM VARCHAR(200), -- "velezay en truc"
   GEORES VARCHAR(200),
   NB_AGREMENTS INT,
   PRIMARY KEY(IDETABLISSEMENT)
);

CREATE TABLE IF NOT EXISTS ACTIVITE(
   IDACTIVITE SERIAL,
   LIBELLE_ACTIVITE VARCHAR(200),
   CATEGORIE_FRAIS BOOLEAN,
   PRIMARY KEY(IDACTIVITE)
);

CREATE TABLE IF NOT EXISTS INSPECTION(
   IDINSPECTION SERIAL,
   NUMERO_INSPECTION VARCHAR(200),
   DATE_INSPECTION DATE,
   SYNTHESE_EVAL VARCHAR(200),
   PREDICTION_IA VARCHAR(200),	
   NUMERO_AGREMENT VARCHAR(200),
   IDETABLISSEMENT INT,
   IDACTIVITE INT,
   PRIMARY KEY(IDINSPECTION),
   FOREIGN KEY(IDETABLISSEMENT) REFERENCES ETABLISSEMENT(IDETABLISSEMENT),
   FOREIGN KEY(IDACTIVITE) REFERENCES ACTIVITE(IDACTIVITE)
);
