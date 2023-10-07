num_1 = float(input("Ingrese el primer numero: \n"))
num_2 = float(input("Ingreses el segundo numero: \n "))
valoraciones = []

if num_1 == num_2:
    VorF = "Verdadero"
    valoraciones.append(VorF)
elif num_1 != num_2:
    VorF = "Verdadero"
    valoraciones.append(VorF)

print("Los numeros son iguales: {} \n Los numeros son diferentes {}: \n El primer numero es mayor al segundo {}: \n El segundo numero es mayor que el primero {}: \n ")
print (valoraciones)