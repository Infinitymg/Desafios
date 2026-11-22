# Desafios

Aqui eu guardo os desafios e exercícios de programação em Python que fui fazendo entre abril e maio de 2026. Começa com listas bem simples e termina em sistema pequeno com menu, arquivo e até álgebra linear com NumPy.

Se for ver só dois, veja o **Desafio 1** e o **Desafio 2**. São os que mais parecem um programa de verdade.

## Como rodar

Cada desafio roda de dentro da própria pasta (alguns arquivos importam outros da mesma pasta). Precisa de Python 3. Do Desafio 4 em diante também precisa do NumPy:

```
pip install numpy
```

Exemplo:

```
cd "Desafios/Desafio 1"
python main.py
```

## O que tem em cada um

**[Desafio 1](Desafios/Desafio%201) - Folha de pagamento.** Menu no terminal pra cadastrar funcionário (estagiário, CLT ou freelancer), gerar o relatório com os descontos e salvar em arquivo. O código tá dividido em módulos dentro da pasta `folha/`. O INSS (8%) e o IRRF (10% pra quem ganha mais de R$ 2.000) são valores fixos que usei pra simplificar, não é a tabela real. Os arquivos `txt` e `funcionarios amigos.txt` são relatórios que salvei testando o programa.

**[Desafio 2](Desafios/Desafio%202) - Loja simples.** Cadastro de produtos com validação, venda com 5% de desconto quando a quantidade passa de 10, pilha com as últimas 5 vendas, relatório e opção de salvar em arquivo. Rode `python main.py` pra usar o menu ou `python teste_loja.py` pra rodar os testes com `assert`.

**[Desafio 3](Desafios/Desafio%203) - Listas.** Nove exercícios curtos: criar e acessar listas, `for` e `while`, `append` e `remove`, pilha, ordenar, lista dentro de lista e list comprehension.

**[Desafio 4](Desafios/Desafio%204) - Matrizes.** Um manual prático com 7 exemplos: criar matriz, acessar e mudar elementos, somar e subtrair, multiplicar, transpor, determinante e inversa.

**[Desafio 5](Desafios/Desafio%205) - Matriz aleatória 3x3.** A mesma coisa feita de duas formas: com lista pura e com NumPy.

**[Desafio 6](Desafios/Desafio%206) - Sistemas lineares.** Problemas de produção (trabalhadores e máquinas, pães e bolos, mistura de produtos químicos) resolvidos com `np.linalg.solve`. Tem também um programa que pede os números de uma matriz 3x3 pro usuário digitar.
