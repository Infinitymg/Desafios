import numpy as np


def main():
    print("=== Exercício 2: Trabalhadores, Máquinas e Horas (3x3) ===\n")

    A = np.array([[4, 2, 3],
                  [3, 3, 2],
                  [5, 1, 4]], dtype=float)
    B = np.array([150, 140, 160], dtype=float)

    det = np.linalg.det(A)
    print(f"Determinante de A: {det:.6f}")

    if np.abs(det) < 1e-10:
        print("Erro: A matriz A não é invertível (determinante ~ 0).")
        print("Não existe solução única.")
        return

    try:
        X = np.linalg.solve(A, B)
        x, y, z = X

        print("\nTaxas de produção:")
        print(f"x = {x:.2f} itens por trabalhador")
        print(f"y = {y:.2f} itens por máquina")
        print(f"z = {z:.2f} itens por hora")

        producao = 6 * x + 3 * y + 5 * z
        print(f"\nProdução com 6 trabalhadores, 3 máquinas e 5 horas: {producao:.2f} itens")

        print("\nVerificação:")
        eq1 = 4 * x + 2 * y + 3 * z
        eq2 = 3 * x + 3 * y + 2 * z
        eq3 = 5 * x + 1 * y + 4 * z
        s1 = f"4x + 2y + 3z = {eq1:.2f} (esperado 150)"
        s2 = f"3x + 3y + 2z = {eq2:.2f} (esperado 140)"
        s3 = f"5x + 1y + 4z = {eq3:.2f} (esperado 160)"
        print(s1)
        print(s2)
        print(s3)

    except np.linalg.LinAlgError:
        print("\nErro: Não foi possível resolver o sistema (matriz singular ou mal-condicionada).")


if __name__ == "__main__":
    main()

