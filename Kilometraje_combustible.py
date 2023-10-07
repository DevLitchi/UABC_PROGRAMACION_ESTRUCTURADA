print("Consumo de combustible por kilometro recorrido")
km = int(input("Ingrese los kilometros recorridos: \n"))
combu = int(input("Cuantos litros se consumieron en dicho recorrido \n"))
relacion = combu / km
print("El uso de gasolina en relacion por kilómetro es: {}".format(relacion))