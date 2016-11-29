# Imprime las tablas de multiplicar

num = int(input("Introduzca un numero"))

for i in range(1,11):
    resultado = i * num
    print("El resultado de %i * %i es %i" % (num, i, resultado))