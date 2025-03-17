# Pedimos al usuario que ingrese su correo electrónico
correo_usuario = input("Ingrese su correo electrónico: ")

# Dividimos el correo electrónico en dos partes: nombre de usuario y dominio
nombre_usuario, dominio = correo_usuario.split('@')

# Creamos un nuevo correo electrónico con el mismo nombre de usuario pero con el dominio "ceu.es"
nuevo_correo = nombre_usuario + '@ceu.es'

# Mostramos el nuevo correo electrónico por pantalla
print("El nuevo correo electrónico es:", nuevo_correo)
