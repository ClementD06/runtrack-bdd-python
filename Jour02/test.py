
import mysql.connector

class Salariee:
    def __init__(self):
        self.cnx = mysql.connector.connect(user='root', password='Choupimolly8490.',
                                            host='localhost', database='personnel')
        self.cursor = self.cnx.cursor()
    
    def create(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.cnx.commit()
    
    def read(self):
        query = "SELECT * FROM employes"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    def update(self, id_salariee, nom, prenom, salaire, id_service):
        query = "UPDATE employes SET nom=%s, prenom=%s, salaire=%s, id_service=%s WHERE id=%s"
        values = (nom, prenom, salaire, id_service, id_salariee)
        self.cursor.execute(query, values)
        self.cnx.commit()
    
    def delete(self, id_salariee):
        query = "DELETE FROM employes WHERE id=%s"
        values = (id_salariee,)
        self.cursor.execute(query, values)
        self.cnx.commit()
    
    def __del__(self):
        self.cursor.close()
        self.cnx.close()
