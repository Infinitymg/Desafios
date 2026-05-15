import numpy as np


def imprimir_matriz_e_vetor(A: np.ndarray, B: np.ndarray) -> None:
    print("Matriz A:")
    for i in range(A.shape[0]):
        linha = " ".join(str(A[i, j]) for j in range(A.shape[1]))
        print(linha)
    print("\nVetor B:")
    print(B)


def resolver(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    det = np.linalg.det(A)
    if np.abs(det) < 1e-10:
        raise np.linalg.LinAlgError(
            "A matriz A é singular (determinante próximo de zero)."
        )

    X = np.linalg.solve(A, B)
    return X


def main():
    # Sistema:
    # 2x + 3y = 8
    # 4x - y = 7
    A = np.array([[2, 3], [4, -1]], dtype=float)
    B = np.array([8, 7], dtype=float)

    imprimir_matriz_e_vetor(A, B)

    X = resolver(A, B)
    x, y = X

    print("\nSolução:")
    print(f"x = {x:.2f}")
    print(f"y = {y:.2f}")

    # Verificação
    print("\nVerificação:")
    print(f"2x + 3y = {2*x + 3*y:.2f} (esperado {B[0]:.2f})")
    print(f"4x - y = {4*x - y:.2f} (esperado {B[1]:.2f})")


if __name__ == "__main__":
    main()

