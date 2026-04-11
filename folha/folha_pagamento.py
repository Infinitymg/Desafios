def ler_texto_nao_vazio(texto):
    while True:
        valor = input(texto).strip()
        if valor:
            return valor
        print("Valor inválido. Digite algo diferente de vazio.")


def ler_numero_positivo(texto):
    while True:
        valor = input(texto).strip().replace(",", ".")
        try:
            numero = float(valor)
            if numero > 0:
                return numero
            print("Informe um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


TIPO_NOME = {
    "estagiario": "Estagiário",
    "clt": "CLT",
    "freelancer": "Freelancer",
}


def escolher_tipo():
    while True:
        tipo = input("Tipo (estagiario/clt/freelancer): ").strip().lower()
        if tipo in ["estagiario", "clt", "freelancer"]:
            return tipo
        print("Tipo inválido. Digite estagiario, clt ou freelancer.")


def cadastrar_funcionario():
    print("\n--- Cadastro de funcionário ---")
    nome = ler_texto_nao_vazio("Nome: ")
    tipo = escolher_tipo()

    if tipo == "estagiario":
        salario = ler_numero_positivo("Salário fixo mensal (R$): ")
        return {"nome": nome, "tipo": tipo, "salario": salario}

    if tipo == "clt":
        salario = ler_numero_positivo("Salário bruto mensal (R$): ")
        return {"nome": nome, "tipo": tipo, "salario": salario}

    horas = ler_numero_positivo("Horas trabalhadas: ")
    valor_hora = ler_numero_positivo("Valor por hora (R$): ")
    return {
        "nome": nome,
        "tipo": tipo,
        "horas": horas,
        "valor_hora": valor_hora,
    }


def calcular_salario(funcionario):
    tipo = funcionario["tipo"]
    if tipo == "estagiario":
        bruto = funcionario["salario"]
        inss = 0.0
        irrf = 0.0
    elif tipo == "clt":
        bruto = funcionario["salario"]
        inss = bruto * 0.08
        irrf = bruto * 0.10 if bruto > 2000 else 0.0
    else:
        bruto = funcionario["valor_hora"] * funcionario["horas"]
        inss = bruto * 0.05
        irrf = 0.0

    liquido = bruto - inss - irrf
    return {
        "nome": funcionario["nome"],
        "tipo": TIPO_NOME[tipo],
        "bruto": bruto,
        "inss": inss,
        "irrf": irrf,
        "liquido": liquido,
    }


def formatar_valor(valor):
    texto = f"R$ {valor:,.2f}"
    texto = texto.replace(",", "X")
    texto = texto.replace(".", ",")
    texto = texto.replace("X", ".")
    return texto


def gerar_relatorio(funcionarios):
    if not funcionarios:
        return "Nenhum funcionário cadastrado."

    linhas = ["=== Relatório de Folha de Pagamento ==="]
    total = 0.0

    for func in funcionarios:
        info = calcular_salario(func)
        linhas.append(f"Nome: {info['nome']}")
        linhas.append(f"Tipo: {info['tipo']}")
        linhas.append(f"Salário Bruto: {formatar_valor(info['bruto'])}")
        linhas.append(f"Desconto INSS: {formatar_valor(info['inss'])}")
        linhas.append(f"Desconto IRRF: {formatar_valor(info['irrf'])}")
        linhas.append(f"Salário Líquido: {formatar_valor(info['liquido'])}")
        linhas.append("------------------------------")
        total += info["liquido"]

    linhas.append(f"Total pago pela empresa: {formatar_valor(total)}")
    return "\n".join(linhas)


def salvar_relatorio(texto):
    nome_arquivo = ler_texto_nao_vazio(
        "Nome do arquivo para salvar (ex: relatorio_folha.txt): "
    )
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(texto)
        print(f"Relatório salvo em: {nome_arquivo}\n")
    except OSError:
        print(
            "Não foi possível salvar o arquivo. "
            "Verifique o caminho e tente novamente."
        )


def mostrar_menu():
    print("\n=== Sistema de Folha de Pagamento ===")
    print("1 - Cadastrar funcionário")
    print("2 - Gerar relatório")
    print("3 - Salvar relatório")
    print("4 - Sair")


def main():
    funcionarios = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            funcionario = cadastrar_funcionario()
            funcionarios.append(funcionario)
            print("Funcionário cadastrado com sucesso!\n")
        elif opcao == "2":
            relatorio = gerar_relatorio(funcionarios)
            print("\n" + relatorio + "\n")
        elif opcao == "3":
            if not funcionarios:
                print("Cadastre pelo menos um funcionário antes de salvar.\n")
            else:
                relatorio = gerar_relatorio(funcionarios)
                salvar_relatorio(relatorio)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")


if __name__ == "__main__":
    main()
