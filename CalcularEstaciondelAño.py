# Calcular estacion del año

mes = int(input('Ingresa el mes del año (1 al 12): '))
#None es para indicar qe una variable no tiene ningun valor

primavera = mes >= 1 and mes <= 3
verano = mes >= 4 and mes <= 6
otoño = mes >= 7 and mes <= 9
invierno = mes >= 10 and mes <= 12

if primavera:
    print('La estacion es primavera')
elif verano:
    print('La estacion es verano')
elif otoño:
    print('La estacion es otoño')
elif invierno:
    print('La estacion es Invierno')
else:
    print('El mes es incorrecto')