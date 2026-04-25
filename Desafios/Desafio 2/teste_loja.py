# teste_loja.py
# Teste automatizado das funções do sistema de loja

from produtos import listar_produtos
from vendas import calcular_venda
from relatorio import gerar_relatorio, salvar_relatorio
import os


def teste_cadastro():
    print("=== Teste: Cadastro de Produtos ===")
    produtos = []

    # Simula cadastro manual
    produtos.append({"nome": "Camiseta", "preco": 50.0, "estoque": 20})
    produtos.append({"nome": "Notebook", "preco": 2500.0, "estoque": 5})
    produtos.append({"nome": "Celular", "preco": 1000.0, "estoque": 10})

    assert len(produtos) == 3
    assert produtos[0]["nome"] == "Camiseta"
    print("Cadastro OK!\n")
    return produtos


def teste_listar(produtos):
    print("=== Teste: Listar Produtos ===")
    listar_produtos(produtos)
    print("Listagem OK!\n")


def teste_calculo_venda():
    print("=== Teste: Cálculo de Venda ===")
    produto = {"nome": "Camiseta", "preco": 50.0, "estoque": 20}

    # Sem desconto (qtd <= 10)
    resultado = calcular_venda(produto, 5)
    assert resultado["valor_bruto"] == 250.0
    assert resultado["desconto"] == 0.0
    assert resultado["valor_final"] == 250.0

    # Com desconto (qtd > 10)
    resultado = calcular_venda(produto, 15)
    assert resultado["valor_bruto"] == 750.0
    assert resultado["desconto"] == 37.5
    assert resultado["valor_final"] == 712.5

    print("Cálculo OK!\n")


def teste_venda_completa(produtos):
    print("=== Teste: Realizar Venda (simulado) ===")
    vendas = []
    pilha_vendas = []

    # Simula o que a função realizar_venda faria
    produto = produtos[0]  # Camiseta
    quantidade = 15
    calculo = calcular_venda(produto, quantidade)
    produto["estoque"] -= quantidade

    venda = {
        "cliente": "João Silva",
        "produto": produto["nome"],
        "quantidade": quantidade,
        "valor_bruto": calculo["valor_bruto"],
        "desconto": calculo["desconto"],
        "valor_final": calculo["valor_final"]
    }
    vendas.append(venda)
    pilha_vendas.append(venda)

    assert produto["estoque"] == 5  # 20 - 15
    assert vendas[0]["valor_final"] == 712.5
    print("Venda simulada OK!\n")
    return vendas, pilha_vendas


def teste_relatorio(vendas, pilha_vendas):
    print("=== Teste: Gerar Relatório ===")
    gerar_relatorio(vendas, pilha_vendas)
    print("Relatório OK!\n")


def teste_salvar(vendas):
    print("=== Teste: Salvar Relatório ===")
    salvar_relatorio(vendas)
    caminho = os.path.join(os.getcwd(), "relatorio_vendas.txt")
    assert os.path.exists(caminho)
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()
        assert "João Silva" in conteudo
        assert "R$ 712.50" in conteudo
    print("Salvamento OK!\n")


def main():
    print("Iniciando testes automatizados...\n")

    produtos = teste_cadastro()
    teste_listar(produtos)
    teste_calculo_venda()
    vendas, pilha_vendas = teste_venda_completa(produtos)

    # Adiciona mais uma venda para testar relatório com múltiplas vendas
    produto2 = produtos[1]  # Notebook
    quantidade2 = 1
    calculo2 = calcular_venda(produto2, quantidade2)
    produto2["estoque"] -= quantidade2

    venda2 = {
        "cliente": "Maria Souza",
        "produto": produto2["nome"],
        "quantidade": quantidade2,
        "valor_bruto": calculo2["valor_bruto"],
        "desconto": calculo2["desconto"],
        "valor_final": calculo2["valor_final"]
    }
    vendas.append(venda2)
    pilha_vendas.append(venda2)

    teste_relatorio(vendas, pilha_vendas)
    teste_salvar(vendas)

    print("Todos os testes passaram com sucesso!")


if __name__ == "__main__":
    main()

