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
                 descripcion TEXT,
                 estado TEXT DEFAULT 'Disponible')''')
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
    listbox_items.delete(0, tk.END)
    conn = sqlite3.connect('laboratorio.db')
    c = conn.cursor()
    c.execute("SELECT * FROM inventario")
    rows = c.fetchall()
    for row in rows:
        listbox_items.insert(tk.END, row)
    conn.close()

def select_item(event):
    try:
        index = listbox_items.curselection()[0]
        selected_item = listbox_items.get(index)
        entry_id.delete(0, tk.END)
        entry_id.insert(tk.END, selected_item[0])
        entry_nombre.delete(0, tk.END)
        entry_nombre.insert(tk.END, selected_item[1])
        entry_cantidad.delete(0, tk.END)
        entry_cantidad.insert(tk.END, selected_item[2])
        entry_descripcion.delete(0, tk.END)
        entry_descripcion.insert(tk.END, selected_item[3])
    except IndexError:
        pass

def clear_entries():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Función para seleccionar todos los ítems
def select_all_items():
    listbox_items.select_set(0, tk.END)

# Función para eliminar los ítems seleccionados
def delete_selected_items():
    selected_indices = listbox_items.curselection()
    if selected_indices:
        confirmed = messagebox.askyesno("Confirmar", "¿Estás seguro que deseas eliminar los items seleccionados?")
        if confirmed:
            for index in selected_indices[::-1]:  # Delete in reverse order to avoid index issues
                id_item = listbox_items.get(index)[0]
                conn = sqlite3.connect('laboratorio.db')
                c = conn.cursor()
                c.execute("DELETE FROM inventario WHERE id = ?", (id_item,))
                conn.commit()
                conn.close()
            clear_entries()
            display_items()

# Función para marcar un ítem como roto
def mark_as_broken():
    id_item = entry_id.get()
    if id_item:
        try:
            id_item = int(id_item)
            conn = sqlite3.connect('laboratorio.db')
            c = conn.cursor()
            c.execute("UPDATE inventario SET estado = 'Roto' WHERE id = ?", (id_item,))
            conn.commit()
            conn.close()
            clear_entries()
            display_items()
        except (ValueError, sqlite3.Error) as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Debe seleccionar un ítem para marcar como roto.")

# Función para marcar un ítem como robado
def mark_as_stolen():
    id_item = entry_id.get()
    if id_item:
        try:
            id_item = int(id_item)
            conn = sqlite3.connect('laboratorio.db')
            c = conn.cursor()
            c.execute("UPDATE inventario SET estado = 'Robado' WHERE id = ?", (id_item,))
            conn.commit()
            conn.close()
            clear_entries()
            display_items()
        except (ValueError, sqlite3.Error) as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Debe seleccionar un ítem para marcar como robado.")

# Función para marcar un ítem como en proceso de arreglo
def mark_as_fixing():
    id_item = entry_id.get()
    if id_item:
        try:
            id_item = int(id_item)
            conn = sqlite3.connect('laboratorio.db')
            c = conn.cursor()
            c.execute("UPDATE inventario SET estado = 'Arreglando' WHERE id = ?", (id_item,))
            conn.commit()
            conn.close()
            clear_entries()
            display_items()
        except (ValueError, sqlite3.Error) as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Debe seleccionar un ítem para marcar como en proceso de arreglo.")

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
    global entry_id, entry_nombre, entry_cantidad, entry_descripcion, listbox_items
    
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

    btn_select_all = tk.Button(root, text="Seleccionar Todos", command=select_all_items)
    btn_select_all.grid(row=6, column=0)

    btn_delete_selected = tk.Button(root, text="Eliminar Seleccionados", command=delete_selected_items)
    btn_delete_selected.grid(row=6, column=1)

    btn_mark_broken = tk.Button(root, text="Marcar como Roto", command=mark_as_broken)
    btn_mark_broken.grid(row=7, column=0)

    btn_mark_stolen = tk.Button(root, text="Marcar como Robado", command=mark_as_stolen)
    btn_mark_stolen.grid(row=7, column=1)

    btn_mark_fixing = tk.Button(root, text="Marcar en Arreglo", command=mark_as_fixing)
    btn_mark_fixing.grid(row=8, column=0, columnspan=2)

    # Lista de items
    listbox_items = tk.Listbox(root)
    listbox_items.grid(row=9, column=0, columnspan=2)
    listbox_items.bind('<<ListboxSelect>>', select_item)

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
