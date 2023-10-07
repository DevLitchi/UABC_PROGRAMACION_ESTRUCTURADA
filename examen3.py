import random
inicio = int(input("Ingrese el valor inicial del rango: "))
final = int(input("Ingrese el valor final del rango: "))
contador = 0

for item in range (100):
    num = random.randint(inicio,final)
    if num%2 == 0:
        contador += 1

print("La cantidad de numeros pares es {}".format(contador))