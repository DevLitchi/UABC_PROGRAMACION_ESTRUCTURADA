import random
import os
def clear_screen():
    os.system('cls')
def cumpleaños(edad):
    for i in range(1, edad + 1):
        print("Cumpliste {} año{}".format(i, 's' if i > 1 else ''))
def pares(dato):
    clear_screen()
    pares = 0
    for i in range(50):
        if dato % 2 == 0:
            pares += 1
    print("Se generaron {} valores pares aleatorios en el rango de 70 números del 18 al 87.".format(pares))
def vocales(texto):
    clear_screen()
    count_no_vocales = 0
    vocales = 0
    for letra in texto:
        if letra not in 'aeiouáéíóúAEIOUÁÉÍÓÚ':
            count_no_vocales += 1
        else:
            vocales += 1
    print("Hay {} letras que no son vocales y {} que son vocales en '{}'".format(count_no_vocales,vocales, texto))
def area_trapecio(base_mayor, base_menor, altura):
    area = ((base_mayor + base_menor) * altura) / 2
    print("El área del trapecio es: {}".format(area))
def inicio():
    menu = "Menu de opciones"   
    print (menu.center(50, "-")) 
def suelo():
    print("-"*50)
"""
se utiliza el método center() para centrar la cadena menu en una línea de 50 caracteres de ancho, utilizando el carácter - como relleno a cada lado de la cadena. 
El resultado es una línea de 50 caracteres de ancho con la cadena menu centrada y rodeada de guiones.
""" 
while True:
    inicio()
    print("\n[A] Calcular la edad\n[B] para contar pares\n[C] contar caracteres no vocales\n[S] para salir")
    opcion = input("Seleccione una opción:").strip().upper()
    suelo()
    if opcion == 'A':
        edad = int(input("¿Cuántos años tiene? "))
        cumpleaños(edad)
    elif opcion == 'B':
        dato = random.randrange(18, 87)
        pares(dato)   
    elif opcion == 'C':
        texto = input("Ingrese una palabra: ")
        vocales(texto)

    elif opcion == 'S':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")