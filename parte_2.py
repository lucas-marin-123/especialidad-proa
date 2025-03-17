agenda = {}

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar todos los contactos")
    print("5. Salir")

def agregar_persona():
    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")
    dni = input("Ingrese el DNI: ")
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[dni] = {'Apellido': apellido, 'Nombre': nombre, 'Email': email, 'Teléfono': telefono}
    print("Persona agregada exitosamente.")

def modificar_persona():
    dni = input("Ingrese el DNI de la persona que desea modificar: ")
    if dni in agenda:
        print("Datos actuales de la persona:")
        print(agenda[dni])
        opcion = input("¿Qué campos desea modificar? (apellido, nombre, email, telefono): ").lower()
        if opcion in agenda[dni]:
            nuevo_valor = input(f"Ingrese el nuevo valor para {opcion}: ")
            agenda[dni][opcion.capitalize()] = nuevo_valor
            print("Persona modificada exitosamente.")
        else:
            print("Campo inválido.")
    else:
        print("Persona no encontrada.")

def eliminar_persona():
    dni = input("Ingrese el DNI de la persona que desea eliminar: ")
    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada exitosamente.")
    else:
        print("Persona no encontrada.")

def mostrar_agenda():
    if agenda:
        print("\nAgenda Telefónica:")
        for dni, datos in agenda.items():
            print(f"DNI: {dni}, Apellido: {datos['Apellido']}, Nombre: {datos['Nombre']}, Email: {datos['Email']}, Teléfono: {datos['Teléfono']}")
    else:
        print("La agenda está vacía.")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        agregar_persona()
    elif opcion == '2':
        modificar_persona()
    elif opcion == '3':
        eliminar_persona()
    elif opcion == '4':
        mostrar_agenda()
    elif opcion == '5':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")
