#créer la base de données "entreprise" avec la table "employes" et ses champs correspondants :

#CREATE DATABASE personnel;
#USE personnel;

#CREATE TABLE employes (
  #id INT PRIMARY KEY AUTO_INCREMENT,
  #nom VARCHAR(255),
  #prenom VARCHAR(255),
  #salaire DECIMAL(10, 2),
  #id_service INT
#);

#Ajouter des employés a la table " employes"

#INSERT INTO employes (nom, prenom, salaire, id_service) 
#VALUES 
#('Dupont', 'Jean', 2500, 1),
#('Lefevre', 'Pierre', 3200, 1),
#('Durand', 'Paul', 2800, 2),
#('Baker', 'Marie', 4100, 2);

#Recuperer les employes a + de 3000 euros

#SELECT * FROM employes WHERE salaire > 3000;

#Resultat de la commande : 

#+----+---------+--------+---------+------------+
#| id | nom     | prenom | salaire | id_service |
#+----+---------+--------+---------+------------+
#|  2 | Lefevre | Pierre | 3200.00 |          1 |
#|  4 | Baker   | Marie  | 4100.00 |          2 |
#+----+---------+--------+---------+------------+

# sur vsc avec code python :

import mysql.connector

# Se connecter à la base de données
cnx = mysql.connector.connect(user='root', password='Choupimolly8490.',
                              host='localhost', database='laplateformej2')

# Récupérer les employés dont le salaire est supérieur à 3000 €
cursor = cnx.cursor()
query = ("SELECT * FROM employes WHERE salaire > 3000")
cursor.execute(query)

# Afficher le résultat en console
for (id, nom, prenom, salaire, id_service) in cursor:
    print("id={}, nom={}, prenom={}, salaire={}, id_service={}".format(id, nom, prenom, salaire, id_service))

# Fermer la connexion
cursor.close()
cnx.close()

#Creer la table service et inserer les valeurs:

#CREATE TABLE services (
#  id INT PRIMARY KEY AUTO_INCREMENT,
#  nom VARCHAR(255)
#);

#INSERT INTO services (nom) VALUES
#('Service A'),
#('Service B'),
#('Service C');

#récupérer tous les employés et leur service respectif 

#SELECT employes.*, services.nom AS service_nom
#FROM employes
#JOIN services ON employes.id_service = services.id;

#ou sur vsc   avec code python :

# Récupérer tous les employés et leur service respectif
cursor = cnx.cursor()
query = ("SELECT employes.*, services.nom AS service_nom "
         "FROM employes "
         "JOIN services ON employes.id_service = services.id")
cursor.execute(query)

# Afficher le résultat en console
for (id, nom, prenom, salaire, id_service, service_nom) in cursor:
    print("id={}, nom={}, prenom={}, salaire={}, id_service={}, service_nom={}".format(id, nom, prenom, salaire, id_service, service_nom))

# Fermer la connexion
cursor.close()
cnx.close()

#resultat du code python affiché : 

#id=1, nom=Dupont, prenom=Jean, salaire=2500.00, id_service=1, service_nom=Service A
#id=2, nom=Lefevre, prenom=Pierre, salaire=3200.00, id_service=1, service_nom=Service A
#id=3, nom=Durand, prenom=Paul, salaire=2800.00, id_service=2, service_nom=Service B
#id=4, nom=Baker, prenom=Marie, salaire=4100.00, id_service=2, service_nom=Service B