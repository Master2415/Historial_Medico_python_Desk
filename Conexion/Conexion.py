import sqlite3

class ConexionBD:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('database/bd_historial_medico.db')
            self.cursor = self.conn.cursor()
            #print("Conexión exitosa a la base de datos")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrarConexion(self):
        self.conn.commit()
        self.conn.close()