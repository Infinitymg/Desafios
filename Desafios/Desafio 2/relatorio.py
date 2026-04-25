# relatorio.py
# Funções para gerar e salvar relatório de vendas

import os


def gerar_relatorio(vendas, pilha_vendas):
    """Exibe o relatório completo das vendas e o total arrecadado."""
    print("\n=== Relatório de Vendas ===")

    if not vendas:
        print("Nenhuma venda realizada.")
        return

    for venda in vendas:
        print(f"\nCliente: {venda['cliente']}")
        print(f"Produto: {venda['produto']}")
        print(f"Quantidade: {venda['quantidade']}")
        print(f"Valor Bruto: R$ {venda['valor_bruto']:.2f}")
        print(f"Desconto: R$ {venda['desconto']:.2f}")
        print(f"Valor Final: R$ {venda['valor_final']:.2f}")

    total = sum(v["valor_final"] for v in vendas)
    print(f"\nTotal arrecadado pela loja: R$ {total:.2f}")

    # Exibe as últimas 5 vendas (pilha)
    if pilha_vendas:
        print("\n--- Últimas vendas realizadas ---")
        for venda in reversed(pilha_vendas):
            print(
                f"- {venda['cliente']} comprou {venda['quantidade']}x "
                f"{venda['produto']} (R$ {venda['valor_final']:.2f})"
            )


def salvar_relatorio(vendas):
    """Salva o relatório em um arquivo de texto."""
    caminho = os.path.join(os.getcwd(), "relatorio_vendas.txt")

    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write("=== Relatório de Vendas ===\n")

            if not vendas:
                arquivo.write("Nenhuma venda realizada.\n")
            else:
                for venda in vendas:
                    arquivo.write(f"\nCliente: {venda['cliente']}\n")
                    arquivo.write(f"Produto: {venda['produto']}\n")
                    arquivo.write(f"Quantidade: {venda['quantidade']}\n")
                    arquivo.write(
                        f"Valor Bruto: R$ {venda['valor_bruto']:.2f}\n"
                    )
                    arquivo.write(
                        f"Desconto: R$ {venda['desconto']:.2f}\n"
                    )
                    arquivo.write(
                        f"Valor Final: R$ {venda['valor_final']:.2f}\n"
                    )

                total = sum(v["valor_final"] for v in vendas)
                arquivo.write(
                    f"\nTotal arrecadado pela loja: R$ {total:.2f}\n"
                )

        print(f"\nRelatório salvo com sucesso em: {caminho}")

    except Exception as e:
        print(f"\nErro ao salvar o relatório: {e}")

