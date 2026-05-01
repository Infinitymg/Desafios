"""
Manual Prático: Introdução ao Uso de Matrizes em Python
Exemplo 5: Transposição de Matrizes

Este código demonstra como realizar a transposição de matrizes,
trocando linhas por colunas.
"""

import numpy as np

print("=== Transposição de Matrizes com NumPy ===\n")

# Matriz original 2x3
matriz = np.array([[1, 2, 3], 
                   [4, 5, 6]])

print("Matriz original (2x3):")
print(matriz)

# Transposição: matriz.T ou np.transpose(matriz)
transposta = matriz.T  # Ou np.transpose(matriz)

print("\nMatriz transposta (3x2):")
print(transposta)

# ========================================
# Usando listas nativas
# ========================================

print("\n=== Transposição com listas nativas ===\n")

# Matriz usando listas
matriz_lista = [[1, 2, 3], 
                [4, 5, 6]]

print("Matriz original:")
for linha in matriz_lista:
    print(linha)

# Transposição usando zip
transposta_lista = list(zip(*matriz_lista))

print("\nMatriz transposta:")
for linha in transposta_lista:
    print(linha)

# ========================================
# Exemplo prático: Dados de estoque
# ========================================

print("\n=== Exemplo prático: Dados de estoque ===\n")

#Dados originais: produtos (linhas) por meses (colunas)
estoque = np.array([
    [100, 80, 120],   # Produto A: 100 unidades em Jan, 80 em Fev, 120 em Mar
    [50, 60, 45],    # Produto B
    [200, 180, 220]  # Produto C
])

print("Estoque por produto (produtos x meses):")
print(estoque)

# Transpor para ter meses por produto
estoque_transposto = estoque.T

print("\nEstoque transposto (meses x produtos):")
print(estoque_transposto)

#Total por produto (soma das colunas originais = linhas transpostas)
total_por_produto = np.sum(estoque, axis=1)
print("\nTotal por produto:")
print("Produto A:", total_por_produto[0])
print("Produto B:", total_por_produto[1])
print("Produto C:", total_por_produto[2])

#Total por mês (soma das linhas originais = colunas transpostas)
total_por_mes = np.sum(estoque, axis=0)
print("\nTotal por mês:")
print("Janeiro:", total_por_mes[0])
print("Fevereiro:", total_por_mes[1])
print("Março:", total_por_mes[2])
