import sqlite3

class ConexionBD:
    def __init__(self):
        self.baseDatos = 'database/bd_historial_medico.db'
        self.conexion = sqlite3.connect(self.baseDatos)
        self.cursor = self.conexion.cursor()

    def closeConnect(self):
        self.conexion.commit()
        self.conexion.close()   