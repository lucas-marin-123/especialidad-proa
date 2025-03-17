# 1. Verificación de números primos en una lista:

numeros = [11, 12, 13, 14, 15]
primos = []
for num in numeros:
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                break
        else:
            primos.append(num)
print("Números primos en la lista:", primos)


#2. Suma de valores pares en un diccionario:

diccionario = {'a': 2, 'b': 5, 'c': 8, 'd': 11}
suma_pares = 0
for valor in diccionario.values():
    if valor % 2 == 0:
        suma_pares += valor
print("La suma de los valores pares en el diccionario es:", suma_pares)


#3. Inversión de cadenas en una lista:

cadenas = ["hola", "adios", "python", "programacion"]
cadenas_invertidas = [cadena[::-1] for cadena in cadenas]
print("Cadenas invertidas:", cadenas_invertidas)


#4. Generación de una lista de factorial de números:

numeros = [3, 4, 5, 6, 7]
factoriales = [1]
for num in numeros:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    factoriales.append(factorial)
print("Factoriales de los números:", factoriales[1:])


#5. Conteo de vocales en un diccionario de cadenas:

diccionario = {'palabra1': 'Python', 'palabra2': 'lenguaje', 'palabra3': 'programación'}
conteo_vocales = {clave: sum(1 for letra in valor if letra.lower() in 'aeiou') for clave, valor in diccionario.items()}
print("Conteo de vocales en el diccionario:", conteo_vocales)


#6. Clasificación de números en una lista de diccionarios:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
clasificados = {'pares': [], 'impares': []}
for num in numeros:
    if num % 2 == 0:
        clasificados['pares'].append(num)
    else:
        clasificados['impares'].append(num)
print("Números clasificados:", clasificados)


#7. Cálculo de la media de los valores de un diccionario:

diccionario = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
suma_valores = sum(diccionario.values())
media = suma_valores / len(diccionario)
print("La media de los valores en el diccionario es:", media)


#8. Impresión de los valores mayores al promedio de una lista:

valores = [15, 20, 25, 30, 35]
promedio = sum(valores) / len(valores)
mayores = [valor for valor in valores if valor > promedio]
print("Valores mayores al promedio:", mayores)


#9. Conteo de letras en una lista de cadenas:

cadenas = ["hola", "mundo", "python", "programacion"]
conteo_letras = {cadena: sum(1 for letra in cadena if letra.isalpha()) for cadena in cadenas}
print("Conteo de letras en las cadenas:", conteo_letras)


#10. Impresión de números primos del 1 al 100:

primos = []
for num in range(2, 101):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                break
        else:
            primos.append(num)
print("Números primos del 1 al 100:", primos)