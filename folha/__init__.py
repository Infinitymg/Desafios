"""Pacote de componentes para o sistema de folha de pagamento."""

from .calculos import (
    VALID_TYPES,
    calcular_salario,
    calcular_salario_clt,
    calcular_salario_estagiario,
    calcular_salario_freelancer,
)
from .entrada import (
    escolher_tipo_funcionario,
    leia_numero_positivo,
    leia_string_nao_vazia,
    obter_dados_funcionario,
)
from .relatorio import (
    exibir_relatorio,
    gerar_relatorio_texto,
    processar_funcionarios,
)
from .arquivo import (
    salvar_relatorio,
    salvar_relatorio_em_arquivo,
)

__all__ = [
    "VALID_TYPES",
    "calcular_salario",
    "calcular_salario_clt",
    "calcular_salario_estagiario",
    "calcular_salario_freelancer",
    "escolher_tipo_funcionario",
    "leia_numero_positivo",
    "leia_string_nao_vazia",
    "obter_dados_funcionario",
    "exibir_relatorio",
    "gerar_relatorio_texto",
    "processar_funcionarios",
    "salvar_relatorio",
    "salvar_relatorio_em_arquivo",
]
