import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# Conexión a la base de datos
def connect_db():
    conn = sqlite3.connect('laboratorio.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS inventario (
                 id INTEGER PRIMARY KEY,
                 nombre TEXT NOT NULL,
                 cantidad INTEGER NOT NULL,
                 descripcion TEXT)''')
    conn.commit()
    conn.close()

# Funciones CRUD
def add_item():
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    descripcion = entry_descripcion.get()
    
    if nombre and cantidad:
        try:
            cantidad = int(cantidad)
            
            conn = sqlite3.connect('laboratorio.db')
            c = conn.cursor()
            c.execute("INSERT INTO inventario (nombre, cantidad, descripcion) VALUES (?, ?, ?)",
                      (nombre, cantidad, descripcion))
            conn.commit()
            conn.close()
            clear_entries()
            display_items()
        except ValueError:
            messagebox.showerror("Error", "Cantidad debe ser un número válido.")
    else:
        messagebox.showerror("Error", "Nombre y Cantidad son obligatorios.")

def update_item():
    id_item = entry_id.get()
    nombre = entry_nombre.get()
    cantidad = entry_cantidad.get()
    descripcion = entry_descripcion.get()
    
    if id_item:
        try:
            id_item = int(id_item)
            cantidad = int(cantidad)
            
            conn = sqlite3.connect('laboratorio.db')
            c = conn.cursor()
            c.execute("UPDATE inventario SET nombre = ?, cantidad = ?, descripcion = ? WHERE id = ?",
                      (nombre, cantidad, descripcion, id_item))
            conn.commit()
            conn.close()
            clear_entries()
            display_items()
        except ValueError:
            messagebox.showerror("Error", "ID y Cantidad deben ser números válidos.")
    else:
        messagebox.showerror("Error", "Debe seleccionar un ítem para actualizar.")

def delete_item():
    id_item = entry_id.get()
    
    if id_item:
        try:
            id_item = int(id_item)
            
            conn = sqlite3.connect('laboratorio.db')
            c = conn.cursor()
            c.execute("DELETE FROM inventario WHERE id = ?", (id_item,))
            conn.commit()
            conn.close()
            clear_entries()
            display_items()
        except ValueError:
            messagebox.showerror("Error", "ID debe ser un número válido.")
    else:
        messagebox.showerror("Error", "Debe seleccionar un ítem para eliminar.")

def display_items():
    # Limpiar tabla antes de actualizarla
    for i in treeview.get_children():
        treeview.delete(i)
    
    conn = sqlite3.connect('laboratorio.db')
    c = conn.cursor()
    c.execute("SELECT * FROM inventario")
    rows = c.fetchall()
    for row in rows:
        treeview.insert('', 'end', values=row)
    conn.close()

def select_item(event):
    try:
        item = treeview.selection()[0]
        values = treeview.item(item, 'values')
        entry_id.delete(0, tk.END)
        entry_id.insert(tk.END, values[0])
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(tk.END, values[1])
        entry_cantidad.delete(0, tk.END)
        entry_cantidad.insert(tk.END, values[2])
        entry_descripcion.delete(0, tk.END)
        entry_descripcion.insert(tk.END, values[3])
    except IndexError:
        pass

def clear_entries():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Función de inicio de sesión
def login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    email_pattern = r'^[a-zA-Z0-9._%+-]+@escuelasproa.edu.ar$'
    
    if re.match(email_pattern, usuario) and contraseña == "Proa2024":
        login_window.destroy()
        main_app()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Interfaz de usuario principal con Tkinter
def main_app():
    global entry_id, entry_nombre, entry_cantidad, entry_descripcion, treeview
    
    root = tk.Tk()
    root.title("Inventario del Laboratorio")

    # Campos de entrada
    tk.Label(root, text="ID").grid(row=0, column=0)
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1)

    tk.Label(root, text="Nombre").grid(row=1, column=0)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=1, column=1)

    tk.Label(root, text="Cantidad").grid(row=2, column=0)
    entry_cantidad = tk.Entry(root)
    entry_cantidad.grid(row=2, column=1)

    tk.Label(root, text="Descripción").grid(row=3, column=0)
    entry_descripcion = tk.Entry(root)
    entry_descripcion.grid(row=3, column=1)

    # Botones
    btn_add = tk.Button(root, text="Agregar", command=add_item)
    btn_add.grid(row=4, column=0)

    btn_update = tk.Button(root, text="Actualizar", command=update_item)
    btn_update.grid(row=4, column=1)

    btn_delete = tk.Button(root, text="Eliminar", command=delete_item)
    btn_delete.grid(row=5, column=0)

    btn_clear = tk.Button(root, text="Limpiar", command=clear_entries)
    btn_clear.grid(row=5, column=1)

    # Tabla
    treeview = tk.ttk.Treeview(root, columns=('ID', 'Nombre', 'Cantidad', 'Descripción'), show='headings')
    treeview.grid(row=6, column=0, columnspan=2)
    treeview.heading('ID', text='ID')
    treeview.heading('Nombre', text='Nombre')
    treeview.heading('Cantidad', text='Cantidad')
    treeview.heading('Descripción', text='Descripción')
    treeview.bind('<<TreeviewSelect>>', select_item)

    # Iniciar la aplicación
    display_items()
    root.mainloop()

# Interfaz de inicio de sesión
def login_screen():
    global entry_usuario, entry_contraseña, login_window
    
    login_window = tk.Tk()
    login_window.title("Inicio de Sesión")

    tk.Label(login_window, text="Usuario").grid(row=0, column=0)
    entry_usuario = tk.Entry(login_window)
    entry_usuario.grid(row=0, column=1)

    tk.Label(login_window, text="Contraseña").grid(row=1, column=0)
    entry_contraseña = tk.Entry(login_window, show="*")
    entry_contraseña.grid(row=1, column=1)

    btn_login = tk.Button(login_window, text="Iniciar Sesión", command=login)
    btn_login.grid(row=2, column=0, columnspan=2)

    login_window.mainloop()

# Iniciar la aplicación
connect_db()
login_screen()
