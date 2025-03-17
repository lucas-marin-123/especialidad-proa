num = int(input("Ingresa un número: "))
es_primo = True
for i in range(2, num):
    if num % i == 0:
        es_primo = False

print("Es primo" if es_primo else "No es primo")