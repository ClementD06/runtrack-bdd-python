import mysql.connector

# Se connecter à la base de données
cnx = mysql.connector.connect(user='root', password='Choupimolly8490.',
                              host='localhost', database='LaPlateforme')

# Calculer la somme des capacités des salles
cursor = cnx.cursor()
query = ("SELECT SUM(capacite) FROM salles")
cursor.execute(query)
somme_capacites = cursor.fetchone()[0]

# Afficher le résultat en console
print(f"La somme des capacités des salles est de {somme_capacites}")

# Fermer la connexion
cursor.close()
cnx.close()

#Affichage en console : 
#La somme des capacités des salles est de 244