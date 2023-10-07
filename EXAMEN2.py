while True:
    num_1 = float(input("Ingrese un número: "))
    num_2 = float(input("Ingrese otro número: "))
    operacion = input("Ingrese la operación que desea realizar: [+] Suma, [-] Resta, [/] División, [*] Multiplicación: ")

    if operacion == '+':
        suma = num_1 + num_2
        print("La suma es: {} ".format(suma))
    elif operacion == '-':
        resta = num_1 - num_2
        print("La resta es: {} ".format(resta))
    elif operacion == '/':
        if num_2 == 0:
            print("No se puede dividir por 0")
        else:
            division = num_1 / num_2
            print("La división es: {} ".format(division))
    elif operacion == '*':
        multiplicacion = num_1 * num_2
        print("La multiplicación es: {}".format(multiplicacion))
    else:
        print("La operación no es válida")

    respuesta = input("¿Desea salir? (s/n): ")
    if respuesta.lower() == "s":
        break