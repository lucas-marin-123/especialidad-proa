def calcular_costo_mano_de_obra(area, costo_por_metro_cuadrado):
    costo = area * costo_por_metro_cuadrado
    return costo

def main():
    largo = float(input("Ingrese el largo de la pared (en metros): "))
    ancho = float(input("Ingrese el ancho de la pared (en metros): "))
    area = largo * ancho

    costo_por_metro_cuadrado = float(input("Ingrese el costo por metro cuadrado de pintura: "))

    costo_mano_de_obra = calcular_costo_mano_de_obra(area, costo_por_metro_cuadrado)
    print("El costo de mano de obra para pintar la pared es: ${:.2f}".format(costo_mano_de_obra))

if __name__ == "__main__":
    main()
