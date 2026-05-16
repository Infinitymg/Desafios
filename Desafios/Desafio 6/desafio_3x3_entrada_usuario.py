import numpy as np


def ler_matriz_3x3():
    print("Digite os coeficientes da matriz A (3x3):")
    A = np.zeros((3, 3), dtype=float)

    for i in range(3):
        for j in range(3):
            A[i, j] = float(input(f"A[{i}][{j}]: "))

    return A


def ler_vetor_B():
    print("\nDigite os termos independentes (B):")
    B = np.zeros(3, dtype=float)

    for i in range(3):
        B[i] = float(input(f"B[{i}]: "))

    return B


def main():
    print("=== Resolução de Sistema 3x3 (AX = B) ===\n")

    A = ler_matriz_3x3()
    B = ler_vetor_B()

    print("\nMatriz A:")
    for i in range(3):
        for j in range(3):
            print(f"{A[i, j]:.0f}", end=" ")
        print()

    print("\nVetor B:")
    print(B)

    det = np.linalg.det(A)
    print(f"\nDeterminante de A: {det:.6f}")

    if np.abs(det) < 1e-10:
        print("\nErro: A matriz A não é invertível (determinante ~ 0).")
        print("O sistema não tem solução única.")
        return

    try:
        X = np.linalg.solve(A, B)
        x, y, z = X

        print("\nSolução:")
        print(f"x = {x:.2f}")
        print(f"y = {y:.2f}")
        print(f"z = {z:.2f}")

        print("\nVerificação (AX):")
        AX = A @ X
        for i in range(3):
            valor_ax = AX[i]
            valor_b = B[i]
            print(f"(AX)[{i}] = {valor_ax:.6f} | B[{i}] = {valor_b:.6f}")

    except np.linalg.LinAlgError:
        print("\nErro: Não foi possível resolver o sistema (matriz singular ou mal-condicionada).")


if __name__ == "__main__":
    main()

