import random

matriz = []
num_linhas = 3
num_colunas = 3
min_valor = 0
max_valor = 9

for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        numero_aleatorio = random.randint(min_valor, max_valor)
        linha.append(numero_aleatorio)
    matriz.append(linha)

for linha in matriz:
    print(linha)
