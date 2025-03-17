import sqlite3

# Conexión a la base de datos (o creación si no existe)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Función para insertar un nuevo usuario (Create)
def create_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    print(f'Usuario {name} creado correctamente.')

# Función para obtener todos los usuarios (Read)
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)

# Función para actualizar la edad de un usuario por su ID (Update)
def update_user_age(user_id, new_age):
    cursor.execute('UPDATE users SET age = ? WHERE id = ?', (new_age, user_id))
    conn.commit()
    print(f'Edad del usuario con ID {user_id} actualizada correctamente.')

# Función para eliminar un usuario por su ID (Delete)
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    print(f'Usuario con ID {user_id} eliminado correctamente.')

# Ejemplo de uso
create_user('Alice', 25)
create_user('Bob', 30)
get_all_users()

update_user_age(1, 26)
get_all_users()

delete_user(2)
get_all_users()

# Cerrar la conexión al finalizar
conn.close()
import sqlite3

# Conexión a la base de datos (o creación si no existe)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# Función para insertar un nuevo usuario (Create)
def create_user(name, age):
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    print(f'Usuario {name} creado correctamente.')

# Función para obtener todos los usuarios (Read)
def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        print(user)

# Función para actualizar la edad de un usuario por su ID (Update)
def update_user_age(user_id, new_age):
    cursor.execute('UPDATE users SET age = ? WHERE id = ?', (new_age, user_id))
    conn.commit()
    print(f'Edad del usuario con ID {user_id} actualizada correctamente.')

# Función para eliminar un usuario por su ID (Delete)
def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    print(f'Usuario con ID {user_id} eliminado correctamente.')

# Ejemplo de uso
create_user('Alice', 25)
create_user('Bob', 30)
get_all_users()

update_user_age(1, 26)
get_all_users()

delete_user(2)
get_all_users()

# Cerrar la conexión al finalizar
conn.close()
