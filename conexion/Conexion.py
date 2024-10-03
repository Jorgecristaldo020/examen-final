import psycopg2

class Conexion:
    """metodo constructor
    """
    def __init__(self):
        self.con = psycopg2.connect("dbname=examenfinaldb user=postgres password=jorge122T")
    
    """getConexion
        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con