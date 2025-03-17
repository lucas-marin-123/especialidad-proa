# Pedimos al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

# Pedimos al usuario que ingrese una vocal
vocal = input("Ingrese una vocal: ")

# Convertimos la vocal ingresada a mayúscula
vocal_mayuscula = vocal.upper()

# Reemplazamos todas las ocurrencias de la vocal en la frase con la versión en mayúscula
frase_con_vocal_mayuscula = frase.replace(vocal, vocal_mayuscula)

# Mostramos la frase con la vocal en mayúscula por pantalla
print("La frase con la vocal en mayúscula es:", frase_con_vocal_mayuscula)
