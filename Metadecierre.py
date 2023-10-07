import random

while True:
    print("Seleccione una de las siguientes opciones: \n[A] para calcular la edad\n[B] para contar pares\n[C] contar caracteres no vocales\n[S] para salir")
    opcion = input("Seleccione una opción: ").strip().upper()

    if opcion == 'A':
        edad = int(input("¿Cuántos años tiene? "))
        for i in range(1, edad + 1):
            print("Cumpliste {} año{}".format(i, 's' if i > 1 else ''))
    
    elif opcion == 'B':
        pares = 0
        for i in range(50):
            dato = random.randrange(18, 87)
            if dato % 2 == 0:
                pares += 1
        print("Se generaron {} valores pares aleatorios en el rango de 70 números del 18 al 87.".format(pares))
    
    elif opcion == 'C':
        texto = input("Ingrese una cadena de texto: ")
        count_no_vocales = 0
        for letra in texto:
            if letra not in 'aeiouáéíóúAEIOUÁÉÍÓÚ':
                count_no_vocales += 1
        print("Hay {} letras que no son vocales en '{}'.format(count_no_vocales, texto)")
    
    elif opcion == 'S':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")