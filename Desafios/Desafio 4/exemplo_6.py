"""
Manual Prático: Introdução ao Uso de Matrizes em Python
Exemplo 6: Calculando Determinantes

Este código demonstra como calcular o determinante de matrizes
usando NumPy.
"""

import numpy as np

print("=== Determinantes de Matrizes com NumPy ===\n")

# Matriz 2x2
A = np.array([[3, 1], 
             [2, 4]])

det_A = np.linalg.det(A)
print("Matriz A (2x2):")
print(A)
print("\nDeterminante de A:", det_A)

# ========================================
# Matriz 3x3
# ========================================

print("\n=== Matriz 3x3 ===\n")

B = np.array([[1, 2, 3], 
             [0, 1, 4], 
             [5, 6, 0]])

det_B = np.linalg.det(B)
print("Matriz B (3x3):")
print(B)
print("\nDeterminante de B:", det_B)

# ========================================
# Verificando invertibilidade
# ========================================

print("\n=== Verificando invertibilidade ===\n")

matrizes = {
    "A (2x2)": np.array([[3, 1], [2, 4]]),
    "B (3x3)": np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]]),
    "Singular (2x2)": np.array([[1, 2], [2, 4]]),  # determinant = 0
    "Identidade 3x3": np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
}

for nome, matriz in matrizes.items():
    det = np.linalg.det(matriz)
    invertivel = "Sim" if det != 0 else "Não"
    print(f"\n{nome}:")
    print(f"  Determinante: {det:.6f}")
    print(f"  Invertível: {invertivel}")

# ========================================
# Exemplo prático: Sistema de equações lineares
# ========================================

print("\n=== Exemplo prático: Sistema de equações ===\n")
print("Sistema:")
print("  3x + y = 10")
print("  2x + 4y = 20")

# Coeficientes
coeficientes = np.array([[3, 1], 
                        [2, 4]])

# Resultados
resultados = np.array([10, 20])

# Determinante do sistema
det_sistema = np.linalg.det(coeficientes)
print(f"\nDeterminante do sistema: {det_sistema}")

if det_sistema != 0:
    # Resolver usando inversa
    inversa = np.linalg.inv(coeficientes)
    solucao = inversa @ resultados
    print(f"Solução: x = {solucao[0]:.2f}, y = {solucao[1]:.2f}")
    
    # Verificação
    print("\nVerificação:")
    print(f"  3*({solucao[0]:.2f}) + 1*({solucao[1]:.2f}) = {3*solucao[0] + 1*solucao[1]:.2f}")
    print(f"  2*({solucao[0]:.2f}) + 4*({solucao[1]:.2f}) = {2*solucao[0] + 4*solucao[1]:.2f}")
else:
    print("Sistema não tem solução única!")
