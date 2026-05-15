import numpy as np


def imprimir_matriz_e_vetor(A: np.ndarray, B: np.ndarray) -> None:
    print("Matriz A:")
    for i in range(A.shape[0]):
        linha = " ".join(str(A[i, j]) for j in range(A.shape[1]))
        print(linha)
    print("\nVetor B:")
    print(B)


def resolver_com_solve(
    A: np.ndarray,
    B: np.ndarray,
    nomes_variaveis=None,
    titulo=None,
    mostrar=True,
):
    if titulo:
        print(f"\n=== {titulo} ===")

    if nomes_variaveis is None:
        nomes_variaveis = [f"x{i}" for i in range(A.shape[1])]

    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    if mostrar:
        imprimir_matriz_e_vetor(A, B)

    try:
        det = np.linalg.det(A)
    except np.linalg.LinAlgError:
        det = 0.0

    if np.abs(det) < 1e-10:
        raise np.linalg.LinAlgError(
            "A matriz A é singular (determinante próximo de zero). "
            "O sistema não tem solução única."
        )

    X = np.linalg.solve(A, B)

    if mostrar:
        print("\nSolução:")
        for nome, valor in zip(nomes_variaveis, X):
            print(f"{nome} = {valor:.2f}")

        # Verificação substituindo valores
        print("\nVerificação:")
        AX = A.dot(X)
        for i in range(A.shape[0]):
            print(f"Equação {i+1}: {AX[i]:.2f} (esperado {B[i]:.2f})")

    return X


def exemplo_2x2():
    # Sistema:
    # 2x + 3y = 8
    # 4x - y = 7
    A = np.array([[2, 3], [4, -1]])
    B = np.array([8, 7])

    X = resolver_com_solve(
        A,
        B,
        nomes_variaveis=["x", "y"],
        titulo="Exemplo 1 (2x2): 2x + 3y = 8 e 4x - y = 7",
    )

    x, y = X
    print("\nVerificação (forma original):")
    print(f"2x + 3y = 2({x:.2f}) + 3({y:.2f}) = {2*x + 3*y:.2f}")
    print(f"4x - y = 4({x:.2f}) - 1({y:.2f}) = {4*x - y:.2f}")


def problema_producao_3x3():
    
    A = np.array([[2, 1, 2], [1, 2, 3], [3, 1, 4]], dtype=float)
    B = np.array([7, 7, 11], dtype=float)

    X = resolver_com_solve(
        A,
        B,
        nomes_variaveis=["x", "y", "z"],
        titulo="Problema 3x3 (Produção): taxa por trabalhador, máquina e hora",
    )

    x, y, z = X
    print("\nProdução adicional (4 trabalhadores, 2 máquinas e 3 horas):")
    producao = 4 * x + 2 * y + 3 * z
    print(f"Produção = {producao:.2f} itens")


def desafio_3x3_input():
    
    print("\n=== Desafio 3x3: entrada do usuário ===")
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
        X = resolver_com_solve(
            A,
            B,
            nomes_variaveis=["x", "y", "z"],
            mostrar=True,
            titulo="Solução do desafio",
        )
        x, y, z = X
        print("\nSolução final (com 2 casas):")
        print(f"x = {x:.2f}")
        print(f"y = {y:.2f}")
        print(f"z = {z:.2f}")

    except np.linalg.LinAlgError as e:
        print(f"\nErro: {e}")


def main():
    print("Sistema de Equações Lineares (matrizes) - NumPy\n")
    print("Escolha uma opção:")
    print("1) Exemplo 2x2 (2x + 3y = 8; 4x - y = 7)")
    print("2) Problema 3x3 (produção: x, y, z)")
    print("3) Desafio 3x3 (entrada do usuário)")

    op = input("Opção (1/2/3): ").strip()

    if op == "1":
        exemplo_2x2()
    elif op == "2":
        problema_producao_3x3()
    elif op == "3":
        desafio_3x3_input()
    else:
        print("Opção inválida. Execute novamente e escolha 1, 2 ou 3.")


if __name__ == "__main__":
    main()

