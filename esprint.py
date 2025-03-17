# Pedimos al usuario que ingrese el número de teléfono en el formato dado
telefono = input("Ingrese el número de teléfono en formato +34-XXXXXXXXX-XX: ")

# Eliminamos el prefijo y la extensión usando slicing
numero_sin_prefijo_y_extension = telefono[5:15]

# Mostramos el número de teléfono sin el prefijo y la extensión
print("El número de teléfono sin el prefijo y la extensión es:", numero_sin_prefijo_y_extension)

# Pedimos al usuario que ingrese el precio del producto en euros con dos decimales
precio = float(input("Ingrese el precio del producto en euros (con dos decimales): "))

# Convertimos el precio a céntimos
precio_cents = int(precio * 100)

# Calculamos el número de euros y de céntimos
euros = precio_cents // 100
centimos = precio_cents % 100

# Mostramos por pantalla el número de euros y de céntimos del precio
print("El precio introducido es de", euros, "euros y", centimos, "céntimos.")

# Pedimos al usuario que ingrese la fecha de nacimiento en formato dd/mm/aaaa
fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")

# Dividimos la fecha en día, mes y año
dia, mes, anio = fecha_nacimiento.split('/')

# Si el día o el mes tienen un solo carácter, añadimos un cero al principio
if len(dia) == 1:
    dia = '0' + dia

if len(mes) == 1:
    mes = '0' + mes

# Mostramos por pantalla el día, mes y año de nacimiento
print("Fecha de nacimiento:")
print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)

# Pedimos al usuario que ingrese los productos de la cesta de la compra separados por comas
productos = input("Ingrese los productos de la cesta de la compra separados por comas: ")

# Dividimos los productos ingresados por el usuario
productos_lista = productos.split(',')

# Mostramos cada producto en una línea distinta
print("Productos en la cesta de la compra:")
for producto in productos_lista:
    print(producto.strip())  # strip() elimina los espacios en blanco al principio y al final de cada producto

# Pedimos al usuario que ingrese el nombre del producto, su precio y el número de unidades
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
unidades = int(input("Ingrese el número de unidades: "))

# Calculamos el coste total
coste_total = precio_unitario * unidades

# Formateamos los valores para que tengan el formato especificado
cadena_formateada = "{} - {:>9.2f} - {:>3d} - {:>11.2f}".format(nombre_producto, precio_unitario, unidades, coste_total)

# Mostramos la cadena formateada por pantalla
print(cadena_formateada)
