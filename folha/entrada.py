def leia_string_nao_vazia(prompt):
    while True:
        texto = input(prompt).strip()
        if texto:
            return texto
        print("Entrada inválida. O valor não pode ficar vazio.")


def leia_numero_positivo(prompt):
    while True:
        valor = input(prompt).strip().replace(",", ".")
        try:
            numero = float(valor)
            if numero > 0:
                return numero
            print("Entrada inválida. Informe um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Informe um número válido.")


def escolher_tipo_funcionario():
    valid_types = {
        "estagiario",
        "clt",
        "freelancer",
    }
    while True:
        tipo = input(
            "Tipo de funcionário (estagiario/clt/freelancer): "
        ).strip().lower()
        if tipo in valid_types:
            return tipo
        print("Tipo inválido. Escolha entre estagiario, clt ou freelancer.")


def obter_dados_funcionario():
    print("\n=== Cadastro de Funcionário ===")
    nome = leia_string_nao_vazia("Nome: ")
    tipo = escolher_tipo_funcionario()

    if tipo == "estagiario":
        salario = leia_numero_positivo(
            "Salário fixo mensal (R$): "
        )
        return {"nome": nome, "tipo": tipo, "salario": salario}

    if tipo == "clt":
        salario = leia_numero_positivo(
            "Salário bruto mensal (R$): "
        )
        return {"nome": nome, "tipo": tipo, "salario": salario}

    horas = leia_numero_positivo("Horas trabalhadas: ")
    valor_hora = leia_numero_positivo(
        "Valor por hora (R$): "
    )
    return {
        "nome": nome,
        "tipo": tipo,
        "horas": horas,
        "valor_hora": valor_hora,
    }
