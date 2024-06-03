import tkinter as tk


class Frame(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.config(bg='#CDD8FF')  # Establecer el color de fondo del frame principal
        self.pack(fill='both', expand=True)  # Empaquetar el frame principal para que ocupe todo el espacio disponible
        self.create_labels()  # Llamar a la función para crear los labels
        self.create_buttons()

    def create_labels(self):
        # Lista de etiquetas y sus textos
        labels_texts = [
            ('Nombre', 'Nombre'),
            ('Apellido Paterno:', 'Apellido Paterno'),
            ('Apellido Materno:', 'Apellido Materno'),
            ('DNI:', 'DNI'),
            ('Fecha Nacimiento:', 'Fecha Nacimiento'),
            ('Edad:', 'Edad'),
            ('Antecedentes:', 'Antecedentes'),
            ('Correo:', 'Correo'),
            ('Telefono:', 'Telefono')
        ]

        # Crear y colocar cada etiqueta en el grid dentro del frame principal
        for index, (label_text, field_name) in enumerate(labels_texts):
            label = tk.Label(self, text=label_text, font=('Arial', 15), bg='#CDD8FF', fg='black')
            label.grid(row=index, column=0, padx=10, pady=5, sticky='w')  # Sticky 'w' alinea a la izquierda

            # Añadir un Entry para el campo correspondiente
            entry = tk.Entry(self, font=('Arial', 15), bg='white', width=30)
            entry.grid(row=index, column=1, columnspan=2, padx=10, pady=5, sticky='ew')  # Expandir el campo horizontalmente

       

    def create_buttons(self):
        
        self.btnNuevo = tk.Button(self, text='Nuevo')
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#158645')
        self.btnNuevo.grid(column=0, row=9, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar')
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#000000', cursor='hand2',activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1, row=9, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar')
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#B00000', cursor='hand2',activebackground='#D27C7C')
        self.btnCancelar.grid(column=2, row=9, padx=10, pady=5) 
        
        
        # Actualizar la geometría de la ventana para que se ajuste al contenido
        self.update_idletasks()
        self.root.geometry(f'{self.winfo_reqwidth()}x{self.winfo_reqheight()}')