import tkinter as tk
from Paciente.gui import Frame


def main():
    root = tk.Tk()
    root.title('Historial Medico')
    root.geometry('400x400')
    root.resizable(0, 0)

    app = Frame(root)
    app.pack(fill='both', expand=True)  # Asegurarse de que el frame ocupe el espacio disponible
    app.mainloop()  # Para que se mantenga ejecutado


if __name__ == '__main__':
    main()
