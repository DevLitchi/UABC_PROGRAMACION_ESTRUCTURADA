while True: 
    nombre = input("Ingresa tu nombre: ")
    if nombre != 'Carlos' and nombre != 'carlos' and nombre != 'CARLOS' and nombre != 'cARLOS':
        print("Hola {} tu no eres mi usuario".format(nombre))
    elif nombre == 'CARLOS':
            print("Hola {} mi usuario".format(nombre))
            break
    elif nombre == 'carlos':
            print("Hola {} mi usuario".format(nombre))
            break
    elif nombre == 'Carlos':
            print("Hola {} mi usuario".format(nombre))
            break
    elif nombre == 'cARLOS':
            print("Hola {} mi usuario".format(nombre))
            break
        