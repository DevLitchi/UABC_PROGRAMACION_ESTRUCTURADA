num_1 = float(input("Ingrese el primer numero:\n"))
num_2 = float(input("Ingreses el segundo numero:\n"))
valoraciones = []
if num_1 == num_2:
    valoraciones.append("Verdadero")
else:
    valoraciones.append("Falso")
if num_1 != num_2:
    valoraciones.append("Verdadero")
else: 
    valoraciones.append("Falso")
if num_1>num_2:
    valoraciones.append("Verdadero")
else:
    valoraciones.append("Falso")

if num_2>num_1:
    valoraciones.append("Verdadero")
else:
    valoraciones.append("Falso")
print("Los dos numeros son iguales : " + valoraciones[0])
print("Los dos numeros son diferentes : " + valoraciones[1])
print("El primero es mayor que el segundo : " + valoraciones[2])
print("El segundo es mayor qu el primero : " + valoraciones[3])