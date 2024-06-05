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
        conexion.cursor.execute(sql) # Ejecuta la consulta SQL utilizando el cursor de la conexión
        conexion.cerrarConexion() # Cierra la conexión a la base de datos
        title = 'Registrar Paciente' # Define el título del mensaje para la ventana emergente de éxito
        mensaje = 'Persona Registrado Exitosamente' # Define el contenido del mensaje para la ventana emergente de éxito
        messagebox.showinfo(title, mensaje) # Muestra una ventana emergente con el título y mensaje definidos indicando éxito
    except:
        title = 'Registrar Persona'
        mensaje = 'Error al Registrar la Persona'
        messagebox.showinfo(title, mensaje)
    

def listarPersonas():
    conexion = ConexionBD()

    listarPersonas = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona

def listarCondicion(where):
    conexion = ConexionBD()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(title, mensaje)
    return listaPersona

def editarDatoPaciente(persona, idPersona):
    conexion = ConexionBD()
    sql = f"""UPDATE Persona SET nombre = '{persona.nombre}', apellidoPaterno = '{persona.apellidoPaterno}',
            apellidoMaterno = '{persona.apellidoMaterno}', dni = '{persona.dni}', fechaNacimiento = '{persona.fechaNacimiento}',
            edad = {persona.edad}, antecedentes = '{persona.antecedentes}', correo = '{persona.correo}', telefono = '{persona.telefono}', activo = 1 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Paciente'
        mensaje = 'Paciente Editado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Paciente'
        mensaje = 'Error al editar paciente'
        messagebox.showinfo(title, mensaje)

def eliminarPaciente(idPersona):
    conexion = ConexionBD()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Paciente'
        mensaje = 'Paciente eliminado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Paciente'
        mensaje = 'Error al eliminar Paciente'
        messagebox.showwarning(title, mensaje)


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
         






