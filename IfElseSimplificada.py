# Convertir numero a Texto

texto = str('')
numero = int(input('Ingresa un numero (1, 2 o 3): '))

if numero == 1:
    texto='Uno'
elif numero==2:
    texto='dos'
elif numero==3:
    texto = 'tres'
else:
    print(f'Escribiste un numero diferente a 1, 2 o 3')

print(f'Numero proporcionado: {numero} : {texto}')