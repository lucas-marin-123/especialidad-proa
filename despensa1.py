# Descripción de la situación:
"""
En esta situación, tenemos una despensa de barrio que vende leche de vaca entera por litro. Se aplican descuentos en función de la cantidad de unidades compradas: 
- 10% de descuento si se compran más de 12 unidades.
- 15% de descuento si se compran más de 24 unidades.
Además, hay un descuento adicional para jubilados: 10% de descuento extra si el cliente es jubilado. Los descuentos son acumulativos.
"""

# Solución implementada en Python:

def calcular_costo(cantidad, precio_unitario, es_jubilado):
    costo_total = cantidad * precio_unitario
    
    # Aplicar descuentos
    if cantidad > 24:
        descuento = 0.15
    elif cantidad > 12:
        descuento = 0.10
    else:
        descuento = 0
    
    # Aplicar descuento adicional para jubilados
    if es_jubilado:
        descuento += 0.10
    
    # Calcular costo final
    costo_final = costo_total * (1 - descuento)
    
    return costo_final

# Ejemplos de uso:
# Calcular costo para un cliente que compra 15 unidades y no es jubilado
costo_cliente_1 = calcular_costo(15, 1000, False)
print("Costo para cliente 1:", costo_cliente_1)

# Calcular costo para un cliente que compra 30 unidades y es jubilado
costo_cliente_2 = calcular_costo(30, 1000, True)
print("Costo para cliente 2:", costo_cliente_2)
