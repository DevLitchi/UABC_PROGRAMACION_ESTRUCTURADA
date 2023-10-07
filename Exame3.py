import random

inicio = int(input("Ingrese el valor inicial del rango: "))
fin = int(input("Ingrese el valor final del rango: "))
contador = 0

for _ in range(100):
    num = random.randint(inicio, fin)
    if num % 2 == 0:
        contador += 1

print("El contador de números pares es:", contador)