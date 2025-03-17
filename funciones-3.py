'''en un curso del colegio se decidio sortear una "torta" entre los mejores promedios del aula.crear un programa en python que permita almacenar los nombres de los alumnos y escoja uno al azar para que sea el ganador'''
import random
alumnos = []
print("Introduce los nombres de los alumnos. Escribe 'fin' para terminar.")
while True:
    nombre = input("Nombre del alumno: ")
    if nombre.lower() == 'fin':
        break
    alumnos.append(nombre)
if alumnos:
    ganador = random.choice(alumnos)
    print(f"El ganador del sorteo es: {ganador}")
else:
    print("No se ingresaron nombres de alumnos para el sorteo.")