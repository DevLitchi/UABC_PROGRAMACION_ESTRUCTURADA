print("Autorizacion de ingreso")
edad = range (0,21)
edad_mujer = range (0,21)
age = int(input("Ingrese la edad del hombre:\n"))
edad_women = int(input("Ingrese la edad de la mujer:\n"))
acompa = input("Estas acompañado por una dama ingrese [SI] o [NO]")
if age not in edad and edad_women not in edad_mujer and acompa == 'SI':
    print("Ingrese")
else:
    print("No puedes ingresar")