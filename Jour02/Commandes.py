import mysql.connector

# Configuration de la connexion à la base de données
config = {
  'user': 'root',
  'password': 'Choupimolly8490.',
  'host': 'localhost',
  'database': 'LaPlateforme',
}
cnx = mysql.connector.connect(**config)

# Récupération des étudiants de la table "students"
cursor = cnx.cursor()
query = ("SELECT * FROM etudiants")
cursor.execute(query)

# Affichage des résultats
for (id, nom, prenom, age, email) in cursor:
  print("{} - {} - {}".format(id, nom, prenom, age, email))