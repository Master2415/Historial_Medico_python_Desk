from HistoriaMedica.Conexion import ConexionBD
from tkinter import messagebox

class Persona:

    def __init__(self, name, lastNameP, lastNameM, dni, nacimiento, edad,
                 antecedentes, correo, telefono):
        
         self.idPersona = None
         self.nombre = name
         self.apellidoPaterno = lastNameP
         self.apellidoMaterno = lastNameM
         self.dni = dni
         self.fechaNacimiento = nacimiento
         self.edad = edad
         self.antecedentes = antecedentes
         self.correo = correo
         self.telefono = telefono
         
    #def __str__(self):
         
         

        


