from optparse import Option
from pickle import TRUE


def mostrar_menu():
    print("\nAgregar telefonica")
    print("1. agregar una persona")
    print("2. modificar una persona")
    print("3. eliminar una persona")
    print("4. mostrar toda la agenda")
    print("5. salir")

def agregar_persona(agenda):
    dni = input("Ingrese el DNI: ")
    if dni in agenda:
        print("El DNI ya está registrado")
    else:
        apellido = input("Ingrese el apellido: ")
        nombre= input("Ingrese el nombre: ")
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda[dni] = {"apellido": apellido, "nombre": nombre, "email": email, "telefono": telefono}
        print("Persona agregada exitosamente.")

def modificar_persona(agenda):
    dni = input("ingresar el dni de la persona a modificar: ")
    if dni not in agenda:
        print("el dni no esta registrado.")
    else:
        print("datos actuales:{agenda[dni]}")
        modificador = input("¿deseas modificar el apellido? (s/n): ")
        if modificador.lower() == 's':
            agenda[dni]["apellido"] = input("¿deseas modificar el apellido? (s/n)")
            modificador = input("¿deseas modificar el apellido? (s/n): ")
        if modificador.lower() == 's':
            agenda[dni]["nombre"] = input("¿deseas modificar el nombre? (s/n)")
            modificador = input("¿deseas modificar el apellido? (s/n): ")
        if modificador.lower() == 's':
            agenda[dni]["email"] = input("¿deseas modificar el email? (s/n)")
            modificador = input("¿deseas modificar el apellido? (s/n): ")
        if modificador.lower() == 's':
            agenda[dni]["telefono"] = input("ingresar el nuevo numro de telefono: ")
        print("datos modificados exitosamente.")
def eliminar_persona(agenda):
    dni = input("ingrese el dni de la persona a eliminar: ")
    if dni in agenda:
        del agenda[dni]
        print("persona eliminada exitosamente.")
    else:
        print("el dni no esta registrado.")

def mostrar_agenda(agenda):
    if not agenda:
        print("la agenda esta vacia.")
    else:
        for dni, datos in agenda.items():
            print(f"dni: {dni}")
            for key,value in datos.items():
                print(f"  {key.capitalize()}: {value}")
            print("-" * 20)

def main():
    agenda = {}
    while TRUE:
        mostrar_menu()
        Option = input("seleccione una opcion: ")
        if Option == '1':
            agregar_persona(agenda)
        elif option == '2':
            modificar_persona(agenda)
        elif Option == '3':
            eliminar_persona(agenda)
        elif Option =='4':
            mostrar_agenda(agenda)
        elif option == '5':
            print("saliendo del programa....")
            break
        else:
            print("opcion no valida. intente nuevamente")

if __name__ == '__name__':
    main()