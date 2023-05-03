import mysql.connector

# Se connecter à la base de données
cnx = mysql.connector.connect(user='root', password='Choupimolly8490.',
                              host='localhost', database='LaPlateforme')

# Calculer la superficie totale de l'ensemble des étages
cursor = cnx.cursor()
query = ("SELECT SUM(superficie) FROM etage")
cursor.execute(query)
superficie_totale = cursor.fetchone()[0]

# Afficher le résultat en console
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

# Fermer la connexion
cursor.close()
cnx.close()

#Affichage en console : 

#La superficie de La Plateforme est de 1000 m2



