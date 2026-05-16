import numpy as np


def main():
    print("=== Exercício 4: Mistura de Produtos Químicos (2x2) ===\n")

    A = np.array([[60, 40],
                  [50, 30]], dtype=float)
    B = np.array([26, 20], dtype=float)

    det = np.linalg.det(A)
    print(f"Determinante de A: {det:.6f}")

    if np.abs(det) < 1e-10:
        print("Erro: A matriz A não é invertível (determinante ~ 0).")
        return

    try:
        X = np.linalg.solve(A, B)
        x = X[0]
        y = X[1]

        print("\nQuantidades do ingrediente X:")
        print(f"x = {x:.2f} unidades por litro de A")
        print(f"y = {y:.2f} unidades por litro de B")

        unidades_x = 70 * x + 50 * y
        print(f"\nUnidades de X em 70 litros de A e 50 litros de B: {unidades_x:.2f} unidades")

        print("\nVerificação:")
        eq1 = 60 * x + 40 * y
        eq2 = 50 * x + 30 * y
        print(f"60x + 40y = {eq1:.2f} (esperado 26)")
        print(f"50x + 30y = {eq2:.2f} (esperado 20)")

    except np.linalg.LinAlgError:
        print("Erro: Não foi possível resolver (matriz singular ou mal-condicionada).")


if __name__ == "__main__":
    main()

