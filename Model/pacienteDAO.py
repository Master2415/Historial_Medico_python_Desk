from Conexion.Conexion import ConexionBD
from tkinter import messagebox

def guardarDatosPersona(persona):
    conexion = ConexionBD()
    sql = f"""INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno,
            dni, fechaNacimiento, edad, antecedentes, correo, telefono, activo) VALUES
            ('{persona.nombre}','{persona.apellidoPaterno}','{persona.apellidoMaterno}',
            '{persona.dni}','{persona.fechaNacimiento}',{persona.edad},'{persona.antecedentes}',
            '{persona.correo}','{persona.telefono}',1)"""
    try:
        conexion.cursor.execute(sql)
        # Ejecuta la consulta SQL utilizando el cursor de la conexión
        conexion.cerrarConexion()
        # Cierra la conexión a la base de datos
        title = 'Registrar Paciente'
        # Define el título del mensaje para la ventana emergente de éxito
        mensaje = 'Persona Registrado Exitosamente'
        # Define el contenido del mensaje para la ventana emergente de éxito
        messagebox.showinfo(title, mensaje)
        # Muestra una ventana emergente con el título y mensaje definidos indicando éxito
    except:
        title = 'Registrar Persona'
        # Define el título del mensaje para la ventana emergente de error
        mensaje = 'Error al Registrar la Persona'
        # Define el contenido del mensaje para la ventana emergente de error
        messagebox.showinfo(title, mensaje)
        # Muestra una ventana emergente con el título y mensaje definidos indicando error

class Persona:

    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, dni,fechaNacimiento, edad, antecedentes, correo, telefono):
        self.idPersona = None # Es autoinclementable en la base de datos
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.dni = dni
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f'Persona[{self.nombre},{self.apellidoPaterno}, {self.apellidoMaterno}, {self.dni},{self.fechaNacimiento},{self.edad},{self.antecedentes},{self.correo},{self.telefono}]'      
         






