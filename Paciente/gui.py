import tkinter as tk

class Frame(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.config(bg='#CDD8FF')  # Establecer el color de fondo del frame principal
        self.pack(fill='both', expand=True)  # Empaquetar el frame principal para que ocupe todo el espacio disponible
        self.create_labels()  # Llamar a la función para crear los labels

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
            label = tk.Label(self, text=label_text, font=('Arial', 15, 'bold'), bg='#CDD8FF', fg='black')
            label.grid(row=index, column=0, padx=10, pady=5, sticky='w')  # Sticky 'w' alinea a la izquierda

            # Añadir un Entry para el campo correspondiente si es necesario
            if field_name != 'Nombre':
                entry = tk.Entry(self, font=('Arial', 15), bg='white')
                entry.grid(row=index, column=1, padx=10, pady=5, sticky='ew')  # Sticky 'ew' expande horizontalmente

        # Actualizar la geometría de la ventana para que se ajuste al contenido
        self.update_idletasks()
        self.root.geometry(f'{self.winfo_reqwidth()}x{self.winfo_reqheight()}')