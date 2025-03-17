def calcular_promedio(notas):
    total = sum(notas)
    promedio = total / len(notas)
    return promedio

def main():
    notas = []
    for i in range(5):
        nota = float(input("Ingrese la nota {}: ".format(i+1)))
        notas.append(nota)
    
    promedio = calcular_promedio(notas)
    print("El promedio de las notas es:", promedio)

if __name__ == "__main__":
    main()
