/* CREATE DATABASE "AlimConfiance" WITH OWNER = postgres ENCODING = 'UTF8'; */

DROP TABLE IF EXISTS INSPECTION;
DROP TABLE IF EXISTS ETABLISSEMENT;
DROP TABLE IF EXISTS ACTIVITE;
DROP TABLE IF EXISTS MOTS_CLES;

CREATE TABLE IF NOT EXISTS ETABLISSEMENT(
   IDETABLISSEMENT SERIAL,
   SIRET VARCHAR(200) ,
   SIREN VARCHAR(200) ,
   NIC VARCHAR(200) ,
   LIBELLE_ETABLISSEMENT VARCHAR(200) ,
   ADRESSE VARCHAR(200) ,
   CODE_POSTAL VARCHAR(200) ,
   DEPARTEMENT VARCHAR(200) ,
   COMMUNE VARCHAR(200) ,
   GEORES VARCHAR(200) ,
   NB_AGREMENTS INTEGER,
   PRIMARY KEY(IDETABLISSEMENT)
);

CREATE TABLE IF NOT EXISTS ACTIVITE(
   IDACTIVITE SERIAL,
   LIBELLE_ACTIVITE VARCHAR(200) ,
   CATEGORIE_FRAIS BOOLEAN,
   PRIMARY KEY(IDACTIVITE)
);

CREATE TABLE IF NOT EXISTS MOTS_CLES(
   IdMotcle SERIAL,
   MOTCLE VARCHAR(200) ,
   PRIMARY KEY(IdMotcle)
);

CREATE TABLE IF NOT EXISTS INSPECTION(
   IDINSPECTION SERIAL,
   NUMERO_INSPECTION VARCHAR(200) ,
   DATE_INSPECTION DATE,
   SYNTHESE_EVAL VARCHAR(200) ,
   NUMERO_AGREMENT VARCHAR(200) ,
   SYNTHESE_AI VARCHAR(200) ,
   IDETABLISSEMENT SERIAL,
   IDACTIVITE SERIAL,
   PRIMARY KEY(IDINSPECTION),
   FOREIGN KEY(IDETABLISSEMENT) REFERENCES ETABLISSEMENT(IDETABLISSEMENT),
   FOREIGN KEY(IDACTIVITE) REFERENCES ACTIVITE(IDACTIVITE)
);

CREATE TABLE MOTCLE_INSPECTION(
   IDINSPECTION SERIAL,
   IdMotcle SERIAL,
   PRIMARY KEY(IDINSPECTION, IdMotcle),
   FOREIGN KEY(IDINSPECTION) REFERENCES INSPECTION(IDINSPECTION),
   FOREIGN KEY(IdMotcle) REFERENCES MOTS_CLES(IdMotcle)
);
