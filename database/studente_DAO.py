from database import DB_connect
from model.studente import Studente


class studente_DAO():

    @staticmethod
    def getStudente(matricola):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = (f"SELECT * "
                 f"FROM studente "
                 f"WHERE matricola = '{matricola}'")
        cursor.execute(query)


        for row in cursor:
            res = Studente(
                matricola=row["matricola"],
                cognome=row["cognome"],
                nome=row["nome"],
                CDS=row["CDS"]
            )

        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getCorsi(matricola):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = (f"SELECT codins "
                 f"FROM iscrizione "
                 f"WHERE matricola = '{matricola}'")
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["codins"])

        cursor.close()
        cnx.close()
        return res

