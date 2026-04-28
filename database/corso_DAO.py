# Add whatever it is needed to interface with the DB Table corso
from database import DB_connect
from database.studente_DAO import studente_DAO
from model.corso import Corso


class corso_DAO():

    @staticmethod
    def getAllCorsi():
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                 FROM corso"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getIscritti(corso):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = (f"SELECT matricola "
                 f"FROM iscrizione "
                 f"WHERE codins = '{corso}'")
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["matricola"])

        cursor.close()
        cnx.close()
        return res

