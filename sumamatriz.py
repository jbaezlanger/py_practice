matriz = []
suma = 0

filas = int(input("ingrese la cantidad de filas: "))
columnas = int(input("ingrese la cantidad de columnas: "))

for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = int(input("ingrese un numero del 1 al 9: "))
        while numero < 1 or numero > 9:
            numero = int(input("error. ingrese un numero del 1 al 9: "))
        fila.append(numero)
        suma = suma + numero
    matriz.append(fila)

print("matriz cargada:")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end=" ")
    print()

print("la suma de la matriz es:", suma)