import tkinter as tk
from tkinter import messagebox

def main_window():
    root = tk.Tk()
    root.title("Gestión de Configuración")
    root.geometry("600x400")

    label = tk.Label(root, text="Bienvenido al Gestor de Configuración", font=("Arial", 16))
    label.pack(pady=20)

    # Botones de gestión
    add_button = tk.Button(root, text="Agregar Configuración", command=lambda: messagebox.showinfo("Info", "Agregar configuración"))
    add_button.pack(pady=5)

    edit_button = tk.Button(root, text="Editar Configuración", command=lambda: messagebox.showinfo("Info", "Editar configuración"))
    edit_button.pack(pady=5)

    delete_button = tk.Button(root, text="Eliminar Configuración", command=lambda: messagebox.showinfo("Info", "Eliminar configuración"))
    delete_button.pack(pady=5)

    root.mainloop()