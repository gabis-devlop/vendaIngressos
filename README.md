# Sistema de Venda de Ingressos para Cinema

## Descrição

Este é um sistema de venda de ingressos para um cinema. O programa gerencia a venda de ingressos com base na idade dos clientes, aplicando descontos quando aplicável, e verificando a forma de pagamento. Ele também controla o estoque de ingressos disponíveis.

## Funcionalidades

- **Cálculo de Preço dos Ingressos:** Calcula o valor total dos ingressos com base na idade e na quantidade de ingressos.
- **Seleção de Filmes:** Apresenta uma lista de filmes disponíveis e permite que o usuário escolha um filme.
- **Controle de Estoque:** Verifica a quantidade de ingressos disponíveis em estoque e atualiza conforme as vendas.
- **Descontos Automáticos:** Aplica descontos automaticamente com base na idade do cliente.
- **Formas de Pagamento:** Suporta várias formas de pagamento, incluindo crédito, débito, Pix e dinheiro.

## Requisitos

- Python 3.x

## Como Usar

1. **Execução do Script:**

   - Execute o script `venda_ingressos.py` no terminal:
     ```sh
     python venda_ingressos.py
     ```

2. **Entrada de Dados:**
   - Insira a idade do cliente.
   - Escolha um filme da lista apresentada.
   - Confirme a escolha do filme.
   - Insira a quantidade de ingressos desejada.
   - Escolha a forma de pagamento.
   - Siga as instruções para concluir o pagamento.

## Estrutura do Código

### Definição de Variáveis e Funções

- `estoque_maximo`: Define o estoque máximo de ingressos disponíveis.
- `valor_ingresso`: Define o valor de cada ingresso.

### Função `calcular_valor_ingresso(idade, quantidade)`

Calcula o valor total dos ingressos com base na idade do cliente e na quantidade de ingressos comprados.

- **Parâmetros:**
  - `idade` (int): Idade do cliente.
  - `quantidade` (int): Quantidade de ingressos desejada.
- **Retorna:**
  - `float`: Valor total dos ingressos.

### Função `escolher_filme(filmes)`

Exibe a lista de filmes disponíveis e permite que o usuário escolha um filme pelo número correspondente.

- **Parâmetros:**
  - `filmes` (list): Lista de filmes disponíveis.
- **Retorna:**
  - `str`: Filme escolhido pelo usuário ou `None` se a operação for cancelada.

### Loop Principal

O loop principal do programa gerencia a entrada de dados do usuário e a lógica de venda de ingressos.

1. **Entrada de Idade:**

   - Solicita a idade do cliente.
   - Determina os filmes disponíveis e o tipo de ingresso com base na idade.
   - Exibe a lista de filmes disponíveis.

2. **Escolha de Filme:**

   - O cliente escolhe um filme da lista.
   - Solicita a confirmação da escolha do filme.

3. **Quantidade de Ingressos:**

   - Solicita a quantidade de ingressos desejada.
   - Verifica se a quantidade solicitada está dentro do limite do estoque.

4. **Cálculo do Valor Total:**

   - Calcula o valor total dos ingressos com base na idade e quantidade.

5. **Formas de Pagamento:**
   - Exibe as formas de pagamento disponíveis.
   - Solicita a escolha da forma de pagamento.
   - Se a forma de pagamento for dinheiro, solicita o valor pago e calcula o troco.
   - Atualiza o estoque de ingressos.

### Fim do Programa

- O programa exibe uma mensagem de esgotamento do estoque quando não houver mais ingressos disponíveis.

## Exemplo de Execução

```sh
Digite sua idade (ou 0 para cancelar): 25
Ingresso inteiro
Filmes disponíveis:
1 - Lobisomem
2 - Seven - Os sete crimes capitais
3 - Capitão América - Admirável mundo novo
4 - Conclave
5 - O auto da compadecida 2
Escolha o número do filme (ou 0 para cancelar): 3
Você escolheu 'Capitão América - Admirável mundo novo'. Confirmar? (s/n ou 0 para cancelar): s
Digite a quantidade de ingressos (ou 0 para cancelar): 2
Valor total: R$40.00
Formas de pagamento disponíveis:
1 - Crédito
2 - Débito
3 - Pix
4 - Dinheiro
Escolha a forma de pagamento (1-4 ou 0 para cancelar): 4
Digite o valor pago (ou 0 para cancelar): 50
Troco: R$10.00
Pagamento aprovado. Ingressos restantes: 5998
Tenha um bom filme!

Estoque de ingressos esgotado.
```
