import numpy as np


def main():
    print("=== Exercício 1: Trabalhadores e Máquinas (2x2) ===\n")

    A = np.array([[5, 3],
                  [8, 2]], dtype=float)
    B = np.array([110, 100], dtype=float)

    X = np.linalg.solve(A, B)
    x = X[0]
    y = X[1]

    print("Taxas de produção:")
    print(f"x = {x:.2f} itens por trabalhador/dia")
    print(f"y = {y:.2f} itens por máquina/dia")

    producao = 10 * x + 4 * y
    print(f"\nProdução com 10 trabalhadores e 4 máquinas: {producao:.2f} itens")

    eq1 = 5 * x + 3 * y
    eq2 = 8 * x + 2 * y
    print("\nVerificação:")
    print(f"5x + 3y = {eq1:.2f} (esperado 110)")
    print(f"8x + 2y = {eq2:.2f} (esperado 100)")


if __name__ == "__main__":
    main()

