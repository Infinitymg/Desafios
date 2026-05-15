import numpy as np


def imprimir_matriz(A: np.ndarray) -> None:
    for i in range(A.shape[0]):
        print(" ".join(f"{A[i, j]:.0f}" for j in range(A.shape[1])))


def resolver(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    det = np.linalg.det(A)
    if np.abs(det) < 1e-10:
        raise np.linalg.LinAlgError(
            "A matriz A não é invertível (determinante próximo de zero)."
        )

    return np.linalg.solve(A, B)


def main():
    print("Desafio 3x3 - entrada do usuário\n")
    print("Digite os coeficientes da matriz A (3x3):")

    A = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = float(input(f"A[{i}][{j}]: "))
            linha.append(valor)
        A.append(linha)

    print("\nDigite os termos independentes (B):")
    B = []
    for i in range(3):
        valor = float(input(f"B[{i}]: "))
        B.append(valor)

    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    try:
        X = resolver(A, B)
        x, y, z = X

        print("\nMatriz A:")
        imprimir_matriz(A)

        print("\nVetor B:")
        print(B)

        print("\nSolução:")
        print(f"x = {x:.2f}")
        print(f"y = {y:.2f}")
        print(f"z = {z:.2f}")

        # Verificação (A@X)
        print("\nVerificação:")
        AX = A.dot(X)
        for i in range(3):
            print(f"Equação {i+1}: {AX[i]:.2f} (esperado {B[i]:.2f})")

    except np.linalg.LinAlgError as e:
        print(f"\nErro: {e}")


if __name__ == "__main__":
    main()

