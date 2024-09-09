import tkinter as tk

class RegistroDeTareas:
    def __init__(self, master):
        self.master = master
        master.title("Registro de Tareas")

        # Crear componentes GUI
        self.etiqueta_titulo = tk.Label(master, text="Registro de Tareas", font=("Arial", 18))
        self.etiqueta_titulo.pack()

        self.etiqueta_descripcion = tk.Label(master, text="Descripción de la tarea:")
        self.etiqueta_descripcion.pack()

        self.campo_descripcion = tk.Text(master, width=30, height=5)
        self.campo_descripcion.pack()

        self.boton_agregar = tk.Button(master, text="Agregar Tarea", command=self.agregar_tarea)
        self.boton_agregar.pack()

        self.boton_eliminar = tk.Button(master, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.pack()

        self.lista_tareas = tk.Listbox(master, width=30)
        self.lista_tareas.pack()

    def agregar_tarea(self):
        descripcion = self.campo_descripcion.get("1.0", tk.END)
        if descripcion:
            self.lista_tareas.insert(tk.END, descripcion)
            self.campo_descripcion.delete("1.0", tk.END)

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            self.lista_tareas.delete(seleccion)

root = tk.Tk()
mi_registro = RegistroDeTareas(root)
root.mainloop()
