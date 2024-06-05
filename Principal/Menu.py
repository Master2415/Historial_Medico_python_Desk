import tkinter as tk
from Paciente.gui import Frame


def main():
    root = tk.Tk()
    root.title('Historial Medico')
    root.resizable(0, 0)

    app = Frame(root)
    app.mainloop()  # Para que se mantenga ejecutado


if __name__ == '__main__':
    main()
