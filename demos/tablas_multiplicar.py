'''
@reegoram
Imprimir las tablas de multiplicar (del 1 al 10) a partir de un número solicitado al usuario.
'''

num = int(input('Indique el número de la tabla de multiplicar: '))

for i in range(1, 11):
    print('%i x %i = %i' %(num, i, num * i))