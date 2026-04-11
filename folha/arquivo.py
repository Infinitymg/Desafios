import os


def salvar_relatorio_em_arquivo(texto):
    while True:
        caminho = input(
            "Informe o caminho do arquivo para salvar o relatório: "
        ).strip()
        if not caminho:
            print("Caminho não pode ser vazio.")
            continue

        diretorio = os.path.dirname(caminho)
        if diretorio and not os.path.exists(diretorio):
            criar = input(
                "O diretório não existe. Deseja criá-lo? (s/n): "
            ).strip().lower()
            if criar == "s":
                try:
                    os.makedirs(diretorio, exist_ok=True)
                except OSError as erro:
                    print(f"Falha ao criar diretório: {erro}")
                    continue
            else:
                continue

        try:
            with open(caminho, "w", encoding="utf-8") as arquivo:
                arquivo.write(texto)
            print(f"Relatório salvo com sucesso em: {caminho}\n")
            break
        except OSError as erro:
            print(f"Erro ao salvar o arquivo: {erro}")
            print("Tente um caminho diferente ou verifique as permissões.")


def salvar_relatorio(
    funcionarios,
    processar_funcionarios,
    gerar_relatorio_texto,
):
    funcionarios_processados = processar_funcionarios(funcionarios)
    relatorio = gerar_relatorio_texto(funcionarios_processados)
    salvar_relatorio_em_arquivo(relatorio)
