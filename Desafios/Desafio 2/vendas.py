# vendas.py
# Funções para calcular e realizar vendas

from produtos import listar_produtos


def calcular_venda(produto, quantidade):
    """Calcula valor bruto, desconto (5% se qtd > 10) e valor final."""
    valor_bruto = produto["preco"] * quantidade
    desconto = 0.0

    if quantidade > 10:
        desconto = valor_bruto * 0.05

    valor_final = valor_bruto - desconto

    return {
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final
    }


def realizar_venda(produtos, vendas, pilha_vendas):
    """Realiza todo o fluxo de venda."""
    print("\n--- Realizar Venda ---")

    if not produtos:
        print("Não há produtos cadastrados para venda.")
        return produtos, vendas, pilha_vendas

    # Nome do cliente
    cliente = input("Nome do cliente: ").strip()
    if not cliente:
        print("Erro: O nome do cliente não pode ser vazio.")
        return produtos, vendas, pilha_vendas

    # Lista produtos
    listar_produtos(produtos)

    # Seleção do produto
    selecao = input("Selecione o produto (número ou nome): ").strip()
    produto_selecionado = None

    # Tenta por índice
    try:
        indice = int(selecao)
        if 1 <= indice <= len(produtos):
            produto_selecionado = produtos[indice - 1]
        else:
            print("Erro: Índice inválido.")
            return produtos, vendas, pilha_vendas
    except ValueError:
        # Tenta por nome (case insensitive)
        for p in produtos:
            if p["nome"].lower() == selecao.lower():
                produto_selecionado = p
                break
        if not produto_selecionado:
            print("Erro: Produto não encontrado.")
            return produtos, vendas, pilha_vendas

    # Quantidade
    try:
        quantidade = int(input("Quantidade desejada: "))
        if quantidade <= 0:
            print("Erro: A quantidade deve ser maior que zero.")
            return produtos, vendas, pilha_vendas
        if quantidade > produto_selecionado["estoque"]:
            print(
                "Erro: Estoque insuficiente. "
                f"Disponível: {produto_selecionado['estoque']} unidades."
            )
            return produtos, vendas, pilha_vendas
    except ValueError:
        print("Erro: Quantidade inválida. Digite um número inteiro.")
        return produtos, vendas, pilha_vendas

    # Calcula a venda
    calculo = calcular_venda(produto_selecionado, quantidade)

    # Atualiza estoque
    produto_selecionado["estoque"] -= quantidade

    # Monta registro da venda
    venda = {
        "cliente": cliente,
        "produto": produto_selecionado["nome"],
        "quantidade": quantidade,
        "valor_bruto": calculo["valor_bruto"],
        "desconto": calculo["desconto"],
        "valor_final": calculo["valor_final"]
    }

    vendas.append(venda)

    # Atualiza pilha das últimas 5 vendas (LIFO)
    pilha_vendas.append(venda)
    if len(pilha_vendas) > 5:
        pilha_vendas.pop(0)

    print("\nVenda realizada com sucesso!")
    print(f"Valor Bruto: R$ {calculo['valor_bruto']:.2f}")
    print(f"Desconto: R$ {calculo['desconto']:.2f}")
    print(f"Valor Final: R$ {calculo['valor_final']:.2f}")

    return produtos, vendas, pilha_vendas

