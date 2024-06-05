import tkinter as tk
import tkcalendar as tc
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, Toplevel
from Model.pacienteDAO import *
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date


class Frame(tk.Frame):

    def __init__(self, root):
        super().__init__(root, width=1280, height=720)
        self.root = root
        self.config(bg='#CDD8FF')  # Establecer el color de fondo del frame principal
        self.pack()  # Empaquetar el frame principal para que ocupe todo el espacio disponible
        self.labels() 
        self.buttons()
        self.entrys()
        self.idPersona = None
        self.deshabilitar_Entrys()
        self.tablaPaciente()

    def labels(self):
        #LABELS
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblApePaterno = tk.Label(self, text='Apellido Paterno: ')
        self.lblApePaterno.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblApePaterno.grid(column=0,row=1, padx=10, pady=5)

        self.lblApeMaterno = tk.Label(self, text='Apellido Materno: ')
        self.lblApeMaterno.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblApeMaterno.grid(column=0,row=2, padx=10, pady=5)

        self.lblDni = tk.Label(self, text='DNI: ')
        self.lblDni.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblDni.grid(column=0,row=3, padx=10, pady=5)

        self.lblFechNacimiento = tk.Label(self, text='Fecha Nacimiento: ')
        self.lblFechNacimiento.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblFechNacimiento.grid(column=0,row=4, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblEdad.grid(column=0,row=5, padx=10, pady=5)

        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblAntecedentes.grid(column=0,row=6, padx=10, pady=5)

        self.lblCorreo = tk.Label(self, text='Correo: ')
        self.lblCorreo.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblCorreo.grid(column=0,row=7, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Telefono: ')
        self.lblTelefono.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0,row=8, padx=10, pady=5)   

    def entrys(self):

        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL',15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApePaterno = tk.StringVar()
        self.entryApePaterno = tk.Entry(self, textvariable=self.svApePaterno)
        self.entryApePaterno.config(width=50, font=('ARIAL',15))
        self.entryApePaterno.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svApeMaterno = tk.StringVar()
        self.entryApeMaterno = tk.Entry(self, textvariable=self.svApeMaterno)
        self.entryApeMaterno.config(width=50, font=('ARIAL',15))
        self.entryApeMaterno.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable=self.svDni)
        self.entryDni.config(width=50, font=('ARIAL',15))
        self.entryDni.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svFecNacimiento = tk.StringVar()
        self.entryFecNacimiento = tk.Entry(self, textvariable=self.svFecNacimiento)
        self.entryFecNacimiento.config(width=50, font=('ARIAL',15))
        self.entryFecNacimiento.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL',15))
        self.entryEdad.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svAntecentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable=self.svAntecentes)
        self.entryAntecedentes.config(width=50, font=('ARIAL',15))
        self.entryAntecedentes.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=('ARIAL',15))
        self.entryCorreo.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL',15))
        self.entryTelefono.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        #ENTRYS BUSCADOR
        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=20, font=('ARIAL',15))
        self.entryBuscarDni.grid(column=4, row=0, padx=10, pady=5, columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=20, font=('ARIAL',15))
        self.entryBuscarApellido.grid(column=4, row=1, padx=10, pady=5, columnspan=2)

    def buttons(self):
        
        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#158645')
        self.btnNuevo.grid(column=0, row=9, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2',activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1, row=9, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_Entrys)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#B00000', cursor='hand2',activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=9, padx=10, pady=5) 

        #LABEL BUSCADOR
        self.lblBuscarDni = tk.Label(self, text='Buscar DNI: ')
        self.lblBuscarDni.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblBuscarDni.grid(column=3, row=0, padx=10, pady=5)

        self.lblBuscarApellido = tk.Label(self, text='Buscar Apellido: ')
        self.lblBuscarApellido.config(font=('ARIAl',15,'bold'), bg='#CDD8FF')
        self.lblBuscarApellido.grid(column=3, row=1, padx=10, pady=5)

        #BUTTON BUSCADOR
        self.btnBuscarCondicion = tk.Button(self, text='Buscar', command = self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#00396F', cursor='hand2',activebackground='#5B8DBD')
        self.btnBuscarCondicion.grid(column=3,row=2, padx=10, pady=5, columnspan=1)

        self.btnLimpiarBuscador = tk.Button(self, text='Limpiar', command = self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#120061', cursor='hand2',activebackground='#7C6DC1')
        self.btnLimpiarBuscador.grid(column=4,row=2, padx=10, pady=5, columnspan=1)

        #BUTTON DE LA TABLA
        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#1E0075', activebackground='#9379E0', cursor='hand2')
        self.btnEditarPaciente.grid(row=11, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command=self.eliminarDatoPaciente )
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.grid(row=11, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente')
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnHistorialPaciente.grid(row=11, column=2, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', activebackground='#5E5E5E', cursor='hand2')
        self.btnSalir.grid(row=11, column=4, padx=10, pady=5)

        self.btnCalendario = tk.Button(self, text='Calendario', command = self.vistaCalendario)
        self.btnCalendario.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#53005B', cursor='hand2',activebackground='#C774CF')
        self.btnCalendario.grid(column=3,row=3, padx=10, pady=5, columnspan=1)

    def vistaCalendario(self):
        self.topCalendario = Toplevel()
        self.topCalendario.title("FECHA NACIMIENTO")
        self.topCalendario.resizable(0,0)
        #self.topCalendario.iconbitmap('img/clinica.ico')
        self.topCalendario.config(bg='#CDD8FF')

        self.svCalendario = StringVar()
        self.calendar = tc.Calendar(self.topCalendario, selectmode='day', year=2015, month=1, day=1)
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1, column = 0)

    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApePaterno.get(), self.svApeMaterno.get(),
            self.svDni.get(), self.svFecNacimiento.get(), self.svEdad.get(), self.svAntecentes.get(),
            self.svCorreo.get(), self.svTelefono.get()
        )

        if self.idPersona == None:
            guardarDatosPersona(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)
    
        self.deshabilitar_Entrys()
        self.tablaPaciente()

    def buscarCondicion(self):
        if len(self.svBuscarDni.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarDni.get())) > 0:
                #where = "WHERE dni = " + self.svBuscarDni.get() + ""  # En esta consulta se debe poner todo el dni
                where = "WHERE dni LIKE '" + self.svBuscarDni.get()+"%' AND activo = 1"
            if (len(self.svBuscarApellido.get())) > 0:
                where = "WHERE apellidoPaterno LIKE '" + self.svBuscarApellido.get()+"%' AND activo = 1"
            
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()


    def deshabilitar_Entrys(self):  
        self.idPersona = None
        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svDni.set('')
        self.svFecNacimiento.set('')
        self.svEdad.set('')
        self.svAntecentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')

        # Desahabilita los campos
        self.entryNombre.config(state='disabled')
        self.entryApePaterno.config(state='disabled')
        self.entryApeMaterno.config(state='disabled')
        self.entryDni.config(state='disabled')
        self.entryFecNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryAntecedentes.config(state='disabled')
        self.entryCorreo.config(state='disabled')
        self.entryTelefono.config(state='disabled')

        # Deshabilito los botones
        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')

    def habilitar(self):
        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svDni.set('')
        self.svFecNacimiento.set('')
        self.svEdad.set('')
        self.svAntecentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')

        self.entryNombre.config(state='normal')
        self.entryApePaterno.config(state='normal')
        self.entryApeMaterno.config(state='normal')
        self.entryDni.config(state='normal')
        self.entryFecNacimiento.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryAntecedentes.config(state='normal')
        self.entryCorreo.config(state='normal')
        self.entryTelefono.config(state='normal')

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal') 

    def editarPaciente(self):
        try:
            # Obtengo los datos
            self.idPersona                  = self.tabla.item(self.tabla.selection())['text'] #Trae el ID
            self.nombrePaciente             = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidoPaternoPaciente    = self.tabla.item(self.tabla.selection())['values'][1]
            self.apellidoMaternoPaciente    = self.tabla.item(self.tabla.selection())['values'][2]
            self.dniPaciente                = self.tabla.item(self.tabla.selection())['values'][3]
            self.fechaNacimientoPaciente    = self.tabla.item(self.tabla.selection())['values'][4]
            self.edadPaciente               = self.tabla.item(self.tabla.selection())['values'][5]
            self.antecedentesPaciente       = self.tabla.item(self.tabla.selection())['values'][6]
            self.correoPaciente             = self.tabla.item(self.tabla.selection())['values'][7]
            self.telefonoPaciente           = self.tabla.item(self.tabla.selection())['values'][8]

            self.habilitar()

            # Se agregan los datos obtenidos en el entry
            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApePaterno.insert(0, self.apellidoPaternoPaciente)
            self.entryApeMaterno.insert(0, self.apellidoMaternoPaciente)
            self.entryDni.insert(0, self.dniPaciente)
            self.entryFecNacimiento.insert(0, self.fechaNacimientoPaciente)
            self.entryEdad.insert(0,self.edadPaciente)
            self.entryAntecedentes.insert(0,self.antecedentesPaciente)
            self.entryCorreo.insert(0,self.correoPaciente)
            self.entryTelefono.insert(0,self.telefonoPaciente)
        except:
            title = 'Editar Paciente'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title, mensaje)

    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)
            
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'No se pudo eliminar paciente'
            messagebox.showinfo(title, mensaje)

    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarDni.set('')
        self.tablaPaciente()

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listarPersonas()
    

        self.tabla = ttk.Treeview(self, column=('Nombre', 'APaterno', 'AMaterno','Dni','FNacimiento','Edad','Antecedentes','Correo','Telefono'))
        self.tabla.grid(column=0, row=10, columnspan=10, sticky='nse')  
        
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=11, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)
        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Ap. Paterno')
        self.tabla.heading('#3',text='Ap. Materno')
        self.tabla.heading('#4',text='Dni')
        self.tabla.heading('#5',text='F. Nacimiento')
        self.tabla.heading('#6',text='Edad')
        self.tabla.heading('#7',text='Antecedentes')
        self.tabla.heading('#8',text='Correo')
        self.tabla.heading('#9',text='Telefono')

        self.tabla.column("#0", anchor=W, width=70)
        self.tabla.column("#1", anchor=W, width=150)
        self.tabla.column("#2", anchor=W, width=120)
        self.tabla.column("#3", anchor=W, width=120)
        self.tabla.column("#4", anchor=W, width=120)
        self.tabla.column("#5", anchor=W, width=100)
        self.tabla.column("#6", anchor=W, width=50)
        self.tabla.column("#7", anchor=W, width=100)
        self.tabla.column("#8", anchor=W, width=250)
        self.tabla.column("#9", anchor=W, width=182)

        for p in self.listaPersona:
            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]), tags=('evenrow',))

    def historiaMedica(self):

        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())['text']
                self.idPersonaHistoria = self.tabla.item(self.tabla.selection())['text']
            if (self.idPersona > 0):
                idPersona = self.idPersona
            
            self.topHistoriaMedica = Toplevel()
            self.topHistoriaMedica.title('HISTORIAL MEDICO')
            self.topHistoriaMedica.resizable(0,0)
            self.topHistoriaMedica.iconbitmap('img/clinica.ico')
            self.topHistoriaMedica.config(bg='#CDD8FF')

            #self.listaHistoria = listarHistoria(idPersona)
            self.tablaHistoria = ttk.Treeview(self.topHistoriaMedica, column=('Apellidos','Fecha Historia', 'Motivo', 'Examen Auxiliar','Tratamiento', 'Detalle'))
            self.tablaHistoria.grid(row=0, column=0, columnspan=7, sticky='nse')

            self.scrollHistoria = ttk.Scrollbar(self.topHistoriaMedica, orient='vertical', command=self.tablaHistoria.yview)
            self.scrollHistoria.grid(row=0, column=8, sticky='nse')
            
            self.tablaHistoria.configure(yscrollcommand=self.scrollHistoria.set)

            self.tablaHistoria.heading('#0', text='ID')
            self.tablaHistoria.heading('#1', text='Nombre y Apellidos')
            self.tablaHistoria.heading('#2', text='Fecha y Hora')
            self.tablaHistoria.heading('#3', text='Motivo')
            self.tablaHistoria.heading('#4', text='Examen Auxiliar')
            self.tablaHistoria.heading('#5', text='Tratamiento')
            self.tablaHistoria.heading('#6', text='Detalle')

            self.tablaHistoria.column('#0', anchor=W, width=50)
            self.tablaHistoria.column('#1', anchor=W, width=150)
            self.tablaHistoria.column('#2', anchor=W, width=100)
            self.tablaHistoria.column('#3', anchor=W, width=120)
            self.tablaHistoria.column('#4', anchor=W, width=250)
            self.tablaHistoria.column('#5', anchor=W, width=200)
            self.tablaHistoria.column('#6', anchor=W, width=450)

            for p in self.listaHistoria:
                self.tablaHistoria.insert('',0, text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6]))

            self.btnGuardarHistoria = tk.Button(self.topHistoriaMedica, text='Agregar Historia', command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#002771', cursor='hand2', activebackground='#7198E0')
            self.btnGuardarHistoria.grid(row=2, column=0, padx=10, pady=5)

            self.btnEditarHistoria = tk.Button(self.topHistoriaMedica, text='Editar Historia', command=self.topEditarHistorialMedico)
            self.btnEditarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#3A005D', cursor='hand2', activebackground='#B47CD6')
            self.btnEditarHistoria.grid(row=2, column=1, padx=10, pady=5)

            self.btnEliminarHistoria = tk.Button(self.topHistoriaMedica, text='Eliminar Historia', command=self.eliminarHistorialMedico)
            self.btnEliminarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#890011', cursor='hand2', activebackground='#DB939C')
            self.btnEliminarHistoria.grid(row=2, column=2, padx=10, pady=5)

            self.btnSalirHistoria = tk.Button(self.topHistoriaMedica, text='Salir', command=self.salirTop)
            self.btnSalirHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2', activebackground='#6F6F6F')
            self.btnSalirHistoria.grid(row=2, column=6, padx=10, pady=5)

            self.idPersona = None
            
        except:
            title = 'Historia Medica'
            mensaje = 'Error al mostrar historial'
            messagebox.showerror(title, mensaje)
            self.idPersona = None

        
    




      