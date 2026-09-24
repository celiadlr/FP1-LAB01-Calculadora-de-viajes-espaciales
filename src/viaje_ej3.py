edad= int(input('Escribe tu edad: '))
nivel_fisico= int(input('Puntúa tu nivel físico: '))
if 1<=nivel_fisico<=10:
    print('Debes introducir valores entre 1-10') 
else:
    nivel_fisico= int(input('Puntúa tu nivel físico: '))


if edad<18:
    print('Debes ser mayor de edad')
elif nivel_fisico<5:
    print('Debes estar en mejor forma')
else:
    print('¡Listo para despegar!')

