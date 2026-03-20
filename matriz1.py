matriz = []
numero = 1

for i in range(3):
    fila = []
    for j in range(3):
        fila.append(numero)
        numero = numero + 1
    matriz.append(fila)

for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=" ")
    print() 