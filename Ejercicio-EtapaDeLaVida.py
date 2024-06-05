#Proporciona tu edad:
# 0-10_: la infancia es increible
#10-20: muchos cambios y mucho estudio
#20-30: amor y comienza el trabajo
#Cualquier otro valor: Etapa de vida no reconocida

edad = int(input('Proporciona tu edad: '))

infancia = 0<= edad <10
cambios = 10<= edad <20
amor = 20<= edad <= 30
mensaje = None
if infancia:
    mensaje = ('La infancia es increible...')
elif cambios:
    mensaje = ('Muchos cambios y mucho estudio...')
elif amor:
    mensaje =('Amor y comienza el trabajo...')
else:
    mensaje = ('Etapa de vida no reconocida...')

print(f'Tu edad es : {edad}, {mensaje}')