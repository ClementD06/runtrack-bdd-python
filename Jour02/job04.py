import mysql.connector

# Se connecter à la base de données
cnx = mysql.connector.connect(user='root', password='Choupimolly8490.',
                              host='localhost', database='LaPlateforme')

# Récupérer tous les noms et capacités de la table "salles"
cursor = cnx.cursor()
query = ("SELECT nom, capacite FROM salles")
cursor.execute(query)

# Stocker les résultats dans une liste
resultats = cursor.fetchall()

# Afficher le résultat en console
print([resultat for resultat in resultats])

# Fermer la connexion
cursor.close()
cnx.close()

#Affichage dans la console : 
#  [('lounge', 100) ('studio son', 5) ('broadcasting', 50) ('bocal peda', 4) ('coworking', 80) ('studio video', 5)]

