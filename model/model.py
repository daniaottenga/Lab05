from database.corso_DAO import corso_DAO
from database.studente_DAO import studente_DAO


class Model:

    def __init__(self):
        pass


    def getAllCorsi(self):
        return corso_DAO.getAllCorsi()


    def getIscritti(self, corso):
        return corso_DAO.getIscritti(corso)


    def getStudente(self, matricola):
        return studente_DAO.getStudente(matricola)


    def getCorsi(self, matricola):
        return studente_DAO.getCorsi(matricola)

