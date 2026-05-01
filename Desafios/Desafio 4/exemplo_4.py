"""
Manual Prático: Introdução ao Uso de Matrizes em Python
Exemplo 4: Multiplicação de Matrizes

Este código demonstra como realizar operações de multiplicação de matrizes
usando NumPy.
"""

import numpy as np

print("=== Multiplicação de Matrizes com NumPy ===\n")

# Matrizes compatíveis: A (2x3) e E (3x2)
A = np.array([[1, 2, 3], 
             [4, 5, 6]])

E = np.array([[7, 8], 
             [9, 10], 
             [11, 12]])

print("Matriz A (2x3):")
print(A)
print("\nMatriz E (3x2):")
print(E)

# Multiplicação: np.dot ou @
F_multi = np.dot(A, E)  # Ou A @ E
print("\nMultiplicação de matrizes (A @ E):")
print(F_multi)

# ========================================
# Exemplo prático: Custos de produção
# ========================================

print("\n=== Exemplo prático: Cálculo de custos totais ===\n")

# Matriz de quantidade de materiais por produto
quantidade = np.array([[10, 5, 2],   # Produto A: 10kg materia1, 5kg materia2, 2kg materia3
                      [8, 3, 1],   # Produto B: 8kg materia1, 3kg materia2, 1kg materia3
                      [5, 8, 3]])  # Produto C: 5kg materia1, 8kg materia2, 3kg materia3

# Matriz de preços por kg de material
precos = np.array([100,   # R$ 100 por kg de materia1
                  50,    # R$ 50 por kg de materia2
                  200])  # R$ 200 por kg de materia3

print("Quantidade de materiais por produto:")
print(quantidade)
print("\nPreços por kg de material:")
print(precos)

# Custo total por produto (multiplicação de matriz por vetor)
custos = quantidade @ precos
print("\nCusto total por produto:")
print(custos)
print("Produto A custou: R$", custos[0])
print("Produto B custou: R$", custos[1])
print("Produto C custou: R$", custos[2])

# ========================================
# Multiplicação Escalar
# ========================================

print("\n=== Multiplicação Escalar ===\n")

matriz = np.array([[1, 2], 
                  [3, 4]])

escalar = 3
resultado = matriz * escalar

print("Matriz original:")
print(matriz)
print("\nEscalar:", escalar)
print("\nResultado (matriz * 3):")
print(resultado)
