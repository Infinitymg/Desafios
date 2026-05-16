import numpy as np


def main():
    print("=== Exercício 3: Pães e Bolos (2x2) ===\n")

    A = np.array([[50, 20],
                  [30, 30]], dtype=float)
    B = np.array([30, 12], dtype=float)

    det = np.linalg.det(A)
    print(f"Determinante de A: {det:.6f}")

    if np.abs(det) < 1e-10:
        print("Erro: A matriz A não é invertível (determinante ~ 0).")
        return

    try:
        X = np.linalg.solve(A, B)
        x = X[0]
        y = X[1]

        print("\nQuantidades por unidade:")
        print(f"x = {x:.2f} kg de farinha por pão")
        print(f"y = {y:.2f} kg de açúcar por bolo")

        farinha = 40 * x + 25 * y
        acucar = 40 * x + 25 * y

        print("\nConsumo para 40 pães e 25 bolos:")
        print(f"Farinha: {farinha:.2f} kg")
        print(f"Açúcar: {acucar:.2f} kg")

        print("\nVerificação:")
        eq1 = 50 * x + 20 * y
        eq2 = 30 * x + 30 * y
        print(f"50x + 20y = {eq1:.2f} (esperado 30)")
        print(f"30x + 30y = {eq2:.2f} (esperado 12)")

    except np.linalg.LinAlgError:
        print("Erro: Não foi possível resolver (matriz singular ou mal-condicionada).")


if __name__ == "__main__":
    main()

