from .calculos import calcular_salario


def formatar_moeda(valor):
    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def processar_funcionarios(funcionarios):
    return [calcular_salario(funcionario) for funcionario in funcionarios]


def gerar_relatorio_texto(funcionarios_processados):
    if not funcionarios_processados:
        return "Nenhum funcionário cadastrado."

    linhas = ["=== Relatório de Folha de Pagamento ==="]
    total_pago = 0.0

    for funcionario in funcionarios_processados:
        linhas.append(f"Nome: {funcionario['nome']}")
        linhas.append(f"Tipo: {funcionario['tipo']}")
        linhas.append(
            f"Salário Bruto: {formatar_moeda(funcionario['salario_bruto'])}"
        )
        lines = [
            (
                "Desconto INSS: "
                f"{formatar_moeda(funcionario['desconto_inss'])}"
            ),
            (
                "Desconto IRRF: "
                f"{formatar_moeda(funcionario['desconto_irrf'])}"
            ),
            (
                "Salário Líquido: "
                f"{formatar_moeda(funcionario['salario_liquido'])}"
            ),
        ]
        linhas.extend(lines)
        linhas.append("------------------------------")
        total_pago += funcionario["salario_liquido"]

    linhas.append(
        f"Total pago pela empresa: {formatar_moeda(total_pago)}"
    )
    return "\n".join(linhas)


def exibir_relatorio(funcionarios):
    funcionarios_processados = processar_funcionarios(funcionarios)
    relatorio = gerar_relatorio_texto(funcionarios_processados)
    print("\n" + relatorio + "\n")
