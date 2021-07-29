# Courses hippiques

## Contexte 

Vous avez à disposition une base de donnée SQL regroupant les courses depuis 2014. Vous avez des informations sur les chevaux, les jockeys ainsi que le type de course (Ici un exemple de donnée que vous allez récupérer: https://aspiturf.com/). Votre mission est d'exploiter cette base de données afin de réaliser un modèle permetttant d'associer une probabilité à chaque cheval d'une course donnée.

## STEP 1 : Création de la DBB

Commandes utilisées :

```
mysql -u username -p password # connect to mysql

SHOW DATABASES # display all databases

CREATE DATABASE pturf1 # create ptrf1 database

USE ptrf1 # Place us in the pturf1 database to make some actions on it

SOURCE data.sql # fill pturf1 database with data.sql data

```
