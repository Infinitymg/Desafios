# main.py
# Programa principal - Menu interativo da loja

from produtos import cadastrar_produto
from vendas import realizar_venda
from relatorio import gerar_relatorio, salvar_relatorio


def main():
    # Listas principais
    produtos = []       # lista de dicionários dos produtos
    vendas = []         # lista de dicionários das vendas
    pilha_vendas = []   # pilha com as últimas 5 vendas

    while True:
        print("\n========== LOJA SIMPLES ==========")
        print("1. Cadastrar produto")
        print("2. Realizar venda")
        print("3. Gerar relatório")
        print("4. Salvar relatório em arquivo")
        print("5. Sair")
        print("==================================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            produtos = cadastrar_produto(produtos)

        elif opcao == "2":
            produtos, vendas, pilha_vendas = realizar_venda(
                produtos, vendas, pilha_vendas
            )

        elif opcao == "3":
            gerar_relatorio(vendas, pilha_vendas)

        elif opcao == "4":
            salvar_relatorio(vendas)

        elif opcao == "5":
            print("\nEncerrando o programa. Até logo!")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()

