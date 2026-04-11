VALID_TYPES = {
    "estagiario": "Estagiário",
    "clt": "CLT",
    "freelancer": "Freelancer",
}


def calcular_salario_estagiario(salario_bruto):
    return {
        "salario_bruto": salario_bruto,
        "desconto_inss": 0.0,
        "desconto_irrf": 0.0,
        "salario_liquido": salario_bruto,
    }


def calcular_salario_clt(salario_bruto):
    desconto_inss = salario_bruto * 0.08
    if salario_bruto > 2000:
        desconto_irrf = salario_bruto * 0.10
    else:
        desconto_irrf = 0.0

    salario_liquido = (
        salario_bruto - desconto_inss - desconto_irrf
    )
    return {
        "salario_bruto": salario_bruto,
        "desconto_inss": desconto_inss,
        "desconto_irrf": desconto_irrf,
        "salario_liquido": salario_liquido,
    }


def calcular_salario_freelancer(valor_hora, horas_trabalhadas):
    salario_bruto = valor_hora * horas_trabalhadas
    desconto_total = salario_bruto * 0.05
    salario_liquido = salario_bruto - desconto_total
    return {
        "salario_bruto": salario_bruto,
        "desconto_inss": desconto_total,
        "desconto_irrf": 0.0,
        "salario_liquido": salario_liquido,
    }


def calcular_salario(funcionario):
    tipo = funcionario["tipo"]
    if tipo == "estagiario":
        resultado = calcular_salario_estagiario(funcionario["salario"])
    elif tipo == "clt":
        resultado = calcular_salario_clt(funcionario["salario"])
    else:
        resultado = calcular_salario_freelancer(
            funcionario["valor_hora"], funcionario["horas"]
        )

    return {
        "nome": funcionario["nome"],
        "tipo": VALID_TYPES[tipo],
        "salario_bruto": resultado["salario_bruto"],
        "desconto_inss": resultado["desconto_inss"],
        "desconto_irrf": resultado["desconto_irrf"],
        "salario_liquido": resultado["salario_liquido"],
    }
