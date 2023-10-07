dias_trabajados = float(input("Ingrese los dias trabajados: \n"))
pago_x_dia = 183.89
horas_ext = float(input("Ingrese el total de las horas extras trabajadas: \n"))
pago_por_horas = 386.90
bono = 500.00
pago_total = dias_trabajados*pago_x_dia + horas_ext * pago_por_horas + bono
print("El total de la nomina es: ${}Mn".format(pago_total))
isr = 0.30
infonavit = 0.15
retencion_info = round(0.15 * pago_total,3)
retencion_isr = round(0.30 * pago_total,3)
total2 = round( pago_total - retencion_info - retencion_isr,3)
print("La retencion por infonavit es ${}Mn y por el ISR es ${}Mn \nEl total de la nomina despues de retenciones es de ${}Mn ".format(retencion_info,retencion_isr,total2))

e B!=C verdadero
j C/B<A falso
 