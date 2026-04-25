# produtos.py
# Funções para cadastrar e listar produtos da loja


def cadastrar_produto(produtos):
    """Solicita nome, preço e estoque, valida e adiciona o produto à lista."""
    print("\n--- Cadastro de Produto ---")

    # Valida nome do produto
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Erro: O nome do produto não pode ser vazio.")
        return produtos

    # Verifica se o produto já existe (case insensitive)
    for p in produtos:
        if p["nome"].lower() == nome.lower():
            print("Erro: Já existe um produto com esse nome.")
            return produtos

    # Valida preço
    try:
        preco = float(input("Preço do produto: R$ "))
        if preco <= 0:
            print("Erro: O preço deve ser maior que zero.")
            return produtos
    except ValueError:
        print("Erro: Preço inválido. Digite um número real.")
        return produtos

    # Valida estoque
    try:
        estoque = int(input("Estoque inicial: "))
        if estoque < 0:
            print("Erro: O estoque não pode ser negativo.")
            return produtos
    except ValueError:
        print("Erro: Estoque inválido. Digite um número inteiro.")
        return produtos

    # Adiciona o produto como dicionário
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")
    return produtos


def listar_produtos(produtos):
    """Exibe todos os produtos cadastrados com índice, preço e estoque."""
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    print("\n--- Produtos Disponíveis ---")
    for indice, produto in enumerate(produtos, start=1):
        print(
            f"{indice}. {produto['nome']} - R$ {produto['preco']:.2f} "
            f"- Estoque: {produto['estoque']}"
        )

