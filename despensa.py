"""una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la
unidad si el cliente compra mas de 12 unidades, el costo tiene un descuento de
un 10% si compra mas de 24 unidades el descuento es del 15% ademas posee el descuento
de jubilados. la promocion de jubilados es sumarle un 10% de descuento si posee
otros descuentos  se suma a los descuentos desarrolle una solucion algoritmica
para saber cuanto debe pagar el cliente
para cada caso hacer:

_una breve descripcion de la situacion comentada en la cabecera del archivo.py
_solucion implentada en python en el mismo archivo donde se detalla la descripcion."""
def calcular_precio(total_unidades, es_jubilado):
    precio_unitario = 1000
    descuento = 0

    # Aplicar descuento por cantidad
    if total_unidades > : 
        descuento = 0.15
    elif total_unidades > :
        descuento = 0.1

    # Aplicar descuento de jubilado
    if es_jubilado:
        descuento += 0.1

    precio_sin_descuento = total_unidades * precio_unitario
    precio_con_descuento = precio_sin_descuento * (1 - descuento)

    return precio_con_descuento

# Ejemplo de uso
unidades_compradas = 30
es_jubilado = True

precio_final = calcular_precio(unidades_compradas, es_jubilado)
print("El precio a pagar es:", precio_final, "pesos.")
