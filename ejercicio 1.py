nombres = []
for i in range(10):
    nombre = input("Ingresa un nombre: ")
    if nombre not in nombres:
        nombres.append(nombre)
    else:
        print("el nombre ya ha sido ingresado. intentalo de nuevo.")
print("los nombres ingresados son:", nombres)

if len(nombres) >= 3:   
    del nombres[2]
if nombres:
    del nombres[-1]
nombres.sort()
print("después de eliminar y ordenar, la lista queda así:", nombres)

persona = {}
persona["nombre"] = input("ingrese nosmbre: ")
persona["apellido"] = input("ingrese apellido: ")
persona["dni"] = input("ingrese DNI: ")
persona["email"] = input("ingrese email: ")
persona["fecha_nacimiento"] = input("ingrese fecha de nacimiento: ")
print("Llos datos de la persona son:", persona)
