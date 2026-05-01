"""
Manual Prático: Introdução ao Uso de Matrizes em Python
Exemplo 7: Inversa de Matriz Usando Determinante

Este código demonstra como calcular a inversa de uma matriz
e verifica a relação com o determinante.
"""

import numpy as np

print("=== Inversa de Matriz ===\n")

# Matriz 2x2
A = np.array([[3, 1], 
             [2, 4]])

det_A = np.linalg.det(A)
print("Matriz A (2x2):")
print(A)
print(f"\nDeterminante de A: {det_A}")

# Verificar se é invertível
if det_A != 0:
    inversa = np.linalg.inv(A)
    print("\nInversa de A:")
    print(inversa)
    
    # Verificação: A @ A^-1 = I
    verificacao = np.dot(A, inversa)
    print("\nVerificação (A @ A^-1 = identidade):")
    print(verificacao)
else:
    print("Matriz não invertível (determinante = 0)")

# ========================================
# Matriz 3x3
# ========================================

print("\n=== Inversa de Matriz 3x3 ===\n")

B = np.array([[1, 2, 3], 
             [0, 1, 4], 
             [5, 6, 0]])

det_B = np.linalg.det(B)
print("Matriz B (3x3):")
print(B)
print(f"\nDeterminante de B: {det_B}")

if det_B != 0:
    inversa_B = np.linalg.inv(B)
    print("\nInversa de B:")
    print(inversa_B)
    
    # Verificação
    verificacao_B = np.dot(B, inversa_B)
    print("\nVerificação (B @ B^-1 = identidade):")
    print(verificacao_B)
else:
    print("Matriz não invertível")

# ========================================
# Exemplo de matriz não invertível
# ========================================

print("\n=== Matriz não invertível ===\n")

singular = np.array([[1, 2], 
                     [2, 4]])

det_singular = np.linalg.det(singular)
print("Matriz singular:")
print(singular)
print(f"\nDeterminante: {det_singular}")

if det_singular != 0:
    inversa_singular = np.linalg.inv(singular)
    print("Inversa:")
    print(inversa_singular)
else:
    print("Matriz não invertível (determinante = 0)")

# ========================================
# Exemplo prático: Resolução de sistemas lineares
# ========================================

print("\n=== Exemplo prático: Resolução de sistemas lineares ===\n")

# Sistema:
# x + 2y = 5
# 3x + 4y = 10

# Matriz de coeficientes
coeficientes = np.array([[1, 2], 
                        [3, 4]])

# Vetor de resultados
resultados = np.array([5, 10])

print("Sistema:")
print("  x + 2y = 5")
print("  3x + 4y = 10")

# Verificar se o sistema tem solução única
det_sistema = np.linalg.det(coeficientes)
print(f"\nDeterminante: {det_sistema}")

if det_sistema != 0:
    # Método 1: Usando inversa
    inversa = np.linalg.inv(coeficientes)
    solucao = inversa @ resultados
    print(f"\nSolução usando inversa:")
    print(f"  x = {solucao[0]}")
    print(f"  y = {solucao[1]}")
    
    # Método 2: Usando solve (mais numérico)
    solucao2 = np.linalg.solve(coeficientes, resultados)
    print(f"\nSolução usando np.linalg.solve:")
    print(f"  x = {solucao2[0]}")
    print(f"  y = {solucao2[1]}")
    
    # Verificação
    print("\nVerificação:")
    print(f"  {solucao[0]} + 2*{solucao[1]} = {solucao[0] + 2*solucao[1]}")
    print(f"  3*{solucao[0]} + 4*{solucao[1]} = {3*solucao[0] + 4*solucao[1]}")
else:
    print("Sistema não tem solução única!")

# ========================================
# Aplicação em criptografia simples
# ========================================

print("\n=== Aplicação em Criptografia (Exemplo Educacional) ===\n")

# Criar uma matriz invertible para codificar
# Nota: Este é um exemplo educacional, não é criptografia segura!

chave = np.array([[3, 5], 
                 [1, 2]])

det_chave = np.linalg.det(chave)
print("Matriz chave para codificação:")
print(chave)
print(f"Determinante: {det_chave}")

if det_chave != 0:
    # Mensagem como matriz (cada letra = número)
    mensagem = np.array([[1, 0],   # O = 1, primeiro caractere
                        [0, 0]])  # placeholder
    
    print("\nMensagem codificada (exemplo):")
    codificada = chave @ mensagem
    print(codificada)
    
    # Decodificar
    inversa_chave = np.linalg.inv(chave)
    decodificada = np.round(inversa_chave @ codificada).astype(int)
    print("\nMensagem decodificada:")
    print(decodificada)
    
    print("\nNota: Este é um exemplo educacional de criptografia matricial.")
    print("Em produção, use bibliotecas criptográficas profissionais.")
else:
    print("Chave inválida para criptografia!")
