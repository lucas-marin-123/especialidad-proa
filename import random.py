import random

def main():
    # Lista para almacenar los nombres de los alumnos
    alumnos = []
    
    # Solicitar el número de alumnos
    num_alumnos = int(input("Ingrese el número de alumnos: "))
    
    # Recolectar los nombres de los alumnos
    for _ in range(num_alumnos):
        nombre = input("Ingrese el nombre del alumno: ")
        alumnos.append(nombre)
    
    # Elegir un ganador al azar
    if alumnos:
        ganador = random.choice(alumnos)
        print(f"¡El ganador de la torta es: {ganador}!")
    else:
        print("No hay alumnos registrados.")

if __name__ == "__main__":
    main()
