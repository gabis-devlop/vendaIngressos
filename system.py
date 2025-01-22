# Define o estoque máximo de ingressos e o valor do ingresso
estoque_maximo = 6000
valor_ingresso = 20.00

# Função para calcular o valor total dos ingressos com base na idade e quantidade
def calcular_valor_ingresso(idade, quantidade):
    if idade < 3:
        return 0
    elif 3 <= idade < 13:
        return quantidade * (valor_ingresso / 2)  # 50% de desconto
    elif 13 <= idade <= 17:
        return quantidade * (valor_ingresso / 2)  # 50% de desconto com carteirinha
    else:
        return quantidade * valor_ingresso  # Valor inteiro

# Função para exibir a lista de filmes e escolher um filme
def escolher_filme(filmes):
    print('Filmes disponíveis:')
    for i, filme in enumerate(filmes, 1):
        print(f"{i} - {filme}")
    while True:
        try:
            escolha_filme = int(input("Escolha o número do filme (ou 0 para cancelar): "))
            if escolha_filme == 0:
                return None  # Cancela a operação
            if 1 <= escolha_filme <= len(filmes):
                return filmes[escolha_filme - 1]  # Retorna o filme escolhido
            print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Escolha inválida. Tente novamente.")

# Loop principal para a venda de ingressos enquanto houver estoque
while estoque_maximo > 0:
    try:
        idade = int(input('Digite sua idade (ou 0 para cancelar): '))
        if idade == 0:
            print("Cancelando a operação...")
            continue  # Reinicia o loop principal
    except ValueError:
        print('Idade inválida. Tente novamente.')
        continue

# Determina os filmes disponíveis e o tipo de ingresso com base na idade
    if idade < 3:
        print('Ingresso gratuito')
        filmes = ['Moana 2']
    elif 3 <= idade < 13:
        print('Ingresso com 50% de desconto')
        filmes = ['Chico Bento e a goiabeira maravilha', 'Deu Preguiça']
    elif 13 <= idade <= 17:
        print('Ingresso com 50% de desconto acompanhado de Carteirinha de Estudante')
        filmes = ['Mufasa - O Rei Leão', 'Sonic 3']
    else:
        print('Ingresso inteiro')
        filmes = ['Lobisomem', 'Seven - Os sete crimes capitais', 'Capitão América - Admirável mundo novo', 'Conclave', 'O auto da compadecida 2']

    filme_escolhido = escolher_filme(filmes)
    if filme_escolhido is None:
        print("Cancelando a operação...")
        continue

# Confirmação da escolha do filme
    while True:
        confirmacao = input(f"Você escolheu '{filme_escolhido}'. Confirmar? (s/n ou 0 para cancelar): ").lower()
        if confirmacao == '0':
            print("Cancelando a operação...")
            break
        if confirmacao == 's':
            break
        print("Escolha Inválida. Tente novamente.")

    if confirmacao == '0':
        continue

# Solicita a quantidade de ingressos
    while True:
        try:
            quantidade_ingressos = int(input("Digite a quantidade de ingressos (ou 0 para cancelar): "))
            if quantidade_ingressos == 0:
                print("Cancelando a operação...")
                break
            break
        except ValueError:
            print("Quantidade inválida. Por favor, insira um número.")

    if quantidade_ingressos == 0:
        continue

# Verifica se a quantidade solicitada está dentro do limite do estoque
    if quantidade_ingressos > estoque_maximo:
        print(f"Desculpe, temos apenas {estoque_maximo} ingressos disponíveis.")
        quantidade_ingressos = estoque_maximo

# Calcula o valor total dos ingressos
    valor_total = calcular_valor_ingresso(idade, quantidade_ingressos)
    print(f"Valor total: R${valor_total:.2f}")

    if idade >= 3:
        while True:
            print("Formas de pagamento disponíveis:\n1 - Crédito\n2 - Débito\n3 - Pix\n4 - Dinheiro")
            try:
                forma_pagamento = int(input("Escolha a forma de pagamento (1-4 ou 0 para cancelar): "))
                if forma_pagamento == 0:
                    print("Cancelando a operação...")
                    break
                if forma_pagamento == 4:  # Pagamento em dinheiro
                    while True:
                        try:
                            valor_pago = float(input("Digite o valor pago (ou 0 para cancelar): "))
                            if valor_pago == 0:
                                print("Cancelando a operação...")
                                break
                            if valor_pago < valor_total:
                                print("Valor insuficiente. Tente novamente.")
                                continue
                            troco = valor_pago - valor_total
                            print(f"Troco: R${troco:.2f}")
                            estoque_maximo -= quantidade_ingressos
                            print(f"Pagamento aprovado. Ingressos restantes: {estoque_maximo}")
                            break
                        except ValueError:
                            print("Valor inválido. Tente novamente.")
                    if valor_pago == 0:
                        break
                else:
                    estoque_maximo -= quantidade_ingressos
                    print(f"Pagamento aprovado. Ingressos restantes: {estoque_maximo}")
                break
            except ValueError:
                print("Forma de pagamento inválida. Tente novamente.")
        if forma_pagamento == 0:
            continue
    else:

# Crianças abaixo de 3 anos não descontam do estoque
        print(f"Ingressos restantes: {estoque_maximo}")

    print("Tenha um bom filme!\n")

print("Estoque de ingressos esgotado.")