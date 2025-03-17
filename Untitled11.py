def calcular_puntos(ganados, empatados):
    puntos_ganados = ganados * 3
    puntos_empatados = empatados * 1
    total_puntos = puntos_ganados + puntos_empatados
    return total_puntos

def main():
    ganados = int(input("Ingrese la cantidad de partidos ganados: "))
    empatados = int(input("Ingrese la cantidad de partidos empatados: "))
    perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))

    puntos = calcular_puntos(ganados, empatados)
    print("El equipo acumula un total de {} puntos en el campeonato.".format(puntos))

if __name__ == "__main__":
    main()
