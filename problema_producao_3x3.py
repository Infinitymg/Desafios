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

    return np.linalg.solve(A, B)


def main():
    # Sistema (produção):
    # 2x + y + 2z = 7
    # x + 2y + 3z = 7
    # 3x + y + 4z = 11
    A = np.array([[2, 1, 2], [1, 2, 3], [3, 1, 4]], dtype=float)
    B = np.array([7, 7, 11], dtype=float)

    imprimir_matriz_e_vetor(A, B)

    X = resolver(A, B)
    x, y, z = X

    print("\nTaxas de produção:")
    print(f"x = {x:.2f} itens por trabalhador")
    print(f"y = {y:.2f} itens por máquina")
    print(f"z = {z:.2f} itens por hora")

    # Produção adicional (4 trabalhadores, 2 máquinas e 3 horas)
    producao = 4 * x + 2 * y + 3 * z
    print("\nProdução adicional:")
    print(
        f"{4} trabalhadores, {2} máquinas e {3} horas -> {producao:.2f} itens"
    )

    # Verificação
    print("\nVerificação:")
    eq1 = 2 * x + 1 * y + 2 * z
    eq2 = 1 * x + 2 * y + 3 * z
    eq3 = 3 * x + 1 * y + 4 * z
    print(f"2x + y + 2z = {eq1:.2f} (esperado {B[0]:.2f})")
    print(f"x + 2y + 3z = {eq2:.2f} (esperado {B[1]:.2f})")
    print(f"3x + y + 4z = {eq3:.2f} (esperado {B[2]:.2f})")


if __name__ == "__main__":
    main()

