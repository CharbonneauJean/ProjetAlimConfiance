/* CREATE DATABASE "AlimConfiance" WITH OWNER = postgres ENCODING = 'UTF8'; */

DROP TABLE IF EXISTS MOTCLE_INSPECTION;
DROP TABLE IF EXISTS INSPECTION;
DROP TABLE IF EXISTS ETABLISSEMENT;
DROP TABLE IF EXISTS ACTIVITE;
DROP TABLE IF EXISTS MOTS_CLES;

CREATE TABLE ETABLISSEMENT(
   idetablissement SERIAL,
   siret VARCHAR(200) ,
   siren VARCHAR(200) ,
   libelle_etablissement VARCHAR(200) ,
   adresse VARCHAR(200) ,
   code_postal VARCHAR(200) ,
   departement INTEGER,
   commune VARCHAR(200) ,
   geores VARCHAR(200) ,
   geores_lat DOUBLE PRECISION,
   geores_lon DOUBLE PRECISION,
   nb_agrements INTEGER,
   commune_norm VARCHAR(200) ,
   evolution_score DOUBLE PRECISION,
   synthese_ai VARCHAR(200) ,
   date_synt_ai DATE,
   PRIMARY KEY(idetablissement)
);

CREATE TABLE ACTIVITE(
   idactivite SERIAL,
   libelle_activite VARCHAR(200) ,
   categorie_frais BOOLEAN,
   PRIMARY KEY(idactivite)
);

CREATE TABLE MOTS_CLES(
   idmotcle SERIAL,
   motcle VARCHAR(200) ,
   PRIMARY KEY(idmotcle)
);

CREATE TABLE INSPECTION(
   idinspection SERIAL,
   numero_inspection VARCHAR(200) ,
   date_inspection DATE,
   synthese_eval VARCHAR(200) ,
   numero_agrement VARCHAR(200) ,
   idetablissement SERIAL,
   idactivite SERIAL,
   PRIMARY KEY(idinspection),
   FOREIGN KEY(idetablissement) REFERENCES ETABLISSEMENT(idetablissement),
   FOREIGN KEY(idactivite) REFERENCES ACTIVITE(idactivite)
);

CREATE TABLE MOTCLE_INSPECTION(
   idinspection SERIAL,
   idmotcle SERIAL,
   PRIMARY KEY(idinspection, idmotcle),
   FOREIGN KEY(idinspection) REFERENCES INSPECTION(idinspection),
   FOREIGN KEY(idmotcle) REFERENCES MOTS_CLES(idmotcle)
);
