# Instrucciones de la tarea:
# Entre 9 y 10: a
# Entre 8 y menor a 9: b
#Entre 0 y menor a 6: F
#Cualquier otro valor: incorrecto

calificacion = int(input('Proporciona tu calificacion: '))

A = 9 <= calificacion == 10 #ESTO SE LEE COMO CALIFICACION ES MAYOR QUE 9 Y CALIFICACION ES IGUAL A 10
B = 8 <= calificacion < 9
C = 7 <= calificacion < 8
D = 6 <= calificacion < 7
F = 0 <= calificacion < 6
nota = None



if A:
    nota = 'A'
    print(f'Tu calificacio fue de {calificacion}, tienes {nota}')
elif B:
        nota = 'B'
        print(f'Tu calificacio fue de {calificacion}, tienes {nota}')
elif C:
        nota = 'C'
        print(f'Tu calificacio fue de {calificacion}, tienes {nota}')
elif D:
        nota = 'D'
        print(f'Tu calificacio fue de {calificacion}, tienes {nota}')
elif F:
    nota = 'F'
    print(f'Tu calificacio fue de {calificacion}, tienes {nota}')
else:
    print(f'Valor Incorrecto')