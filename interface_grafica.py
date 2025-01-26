import tkinter as tk
from tkinter import messagebox, ttk

# Variáveis globais
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

# Função para exibir a mensagem de confirmação
def confirmar_compra():
    global estoque_maximo
    try:
        idade = int(entry_idade.get())
        quantidade_ingressos = int(entry_quantidade.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para idade e quantidade.")
        return

    if quantidade_ingressos > estoque_maximo:
        messagebox.showinfo("Estoque", f"Desculpe, temos apenas {estoque_maximo} ingressos disponíveis.")
        quantidade_ingressos = estoque_maximo

    valor_total = calcular_valor_ingresso(idade, quantidade_ingressos)
    filme_escolhido = combo_filmes.get()

    if idade >= 3:
        forma_pagamento = combo_pagamento.get()
        if forma_pagamento == "Dinheiro":
            try:
                valor_pago = float(entry_valor_pago.get())
                if valor_pago < valor_total:
                    messagebox.showerror("Erro", "Valor insuficiente. Tente novamente.")
                    return
                troco = valor_pago - valor_total
                messagebox.showinfo("Compra Confirmada", f"Compra de {quantidade_ingressos} ingresso(s) para '{filme_escolhido}' confirmada.\nValor total: R${valor_total:.2f}\nTroco: R${troco:.2f}\nIngressos restantes: {estoque_maximo - quantidade_ingressos}")
            except ValueError:
                messagebox.showerror("Erro", "Valor pago inválido. Tente novamente.")
                return
        else:
            messagebox.showinfo("Compra Confirmada", f"Compra de {quantidade_ingressos} ingresso(s) para '{filme_escolhido}' confirmada.\nValor total: R${valor_total:.2f}\nIngressos restantes: {estoque_maximo - quantidade_ingressos}")
    else:
        messagebox.showinfo("Compra Confirmada", f"Compra de {quantidade_ingressos} ingresso(s) para '{filme_escolhido}' confirmada.\nValor total: R${valor_total:.2f}\nIngressos restantes: {estoque_maximo}")

    estoque_maximo -= quantidade_ingressos

    if estoque_maximo <= 0:
        messagebox.showinfo("Estoque Esgotado", "Estoque de ingressos esgotado.")
        janela.destroy()
        return

    # Limpa os campos para nova compra
    entry_idade.delete(0, tk.END)
    combo_filmes.set('')
    entry_quantidade.delete(0, tk.END)
    combo_pagamento.set('')
    entry_valor_pago.delete(0, tk.END)
    lbl_valor_pago.grid_remove()
    entry_valor_pago.grid_remove()

# Função para atualizar os filmes com base na idade
def atualizar_filmes():
    try:
        idade = int(entry_idade.get())
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira uma idade válida.")
        return
    if idade < 3:
        filmes = ['Moana 2']
    elif 3 <= idade < 13:
        filmes = ['Chico Bento e a Goiabeira Maravilhosa', 'Deu Preguiça']
    elif 13 <= idade <= 17:
        filmes = ['Mufasa - O Rei Leão', 'Sonic 3']
    else:
        filmes = ['Lobisomem', 'Seven - Os Sete Crimes Capitais', 'Capitão América - Admirável Mundo Novo', 'Conclave', 'O Auto da Compadecida 2']

    combo_filmes['values'] = filmes
    if filmes:
        combo_filmes.current(0)
    else:
        combo_filmes.set('')

# Função principal para a interface gráfica
def iniciar_interface():
    global entry_idade, entry_quantidade, combo_filmes, combo_pagamento, entry_valor_pago, lbl_valor_pago, janela

    # Configuração da janela principal
    janela = tk.Tk()
    janela.title("Venda de Ingressos para Cinema")
    janela.configure(bg="#f0f0f0")

    # Container principal
    container = ttk.Frame(janela, padding="20 20 20 20")
    container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    janela.columnconfigure(0, weight=1)
    janela.rowconfigure(0, weight=1)

    # Estilo para widgets
    style = ttk.Style()
    style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
    style.configure("TEntry", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12))
    style.configure("TCombobox", font=("Arial", 12))

    # Labels e entradas para a idade
    lbl_idade = ttk.Label(container, text="Digite sua idade:")
    lbl_idade.grid(row=0, column=0, padx=10, pady=5, sticky="E")
    entry_idade = ttk.Entry(container, width=30)
    entry_idade.grid(row=0, column=1, padx=10, pady=5, sticky="W")

    # Botão para atualizar a lista de filmes
    btn_atualizar_filmes = ttk.Button(container, text="Atualizar Filmes", command=atualizar_filmes)
    btn_atualizar_filmes.grid(row=1, column=0, columnspan=2, pady=5)

    # Lista de filmes disponíveis
    lbl_filme = ttk.Label(container, text="Escolha o filme:")
    lbl_filme.grid(row=2, column=0, padx=10, pady=5, sticky="E")
    combo_filmes = ttk.Combobox(container, state="readonly", width=28)
    combo_filmes.grid(row=2, column=1, padx=10, pady=5, sticky="W")

    # Entrada para a quantidade de ingressos
    lbl_quantidade = ttk.Label(container, text="Quantidade de ingressos:")
    lbl_quantidade.grid(row=3, column=0, padx=10, pady=5, sticky="E")
    entry_quantidade = ttk.Entry(container, width=30)
    entry_quantidade.grid(row=3, column=1, padx=10, pady=5, sticky="W")

    # Opções de pagamento
    lbl_pagamento = ttk.Label(container, text="Forma de pagamento:")
    lbl_pagamento.grid(row=4, column=0, padx=10, pady=5, sticky="E")
    formas_pagamento = ['Crédito', 'Débito', 'Pix', 'Dinheiro']
    combo_pagamento = ttk.Combobox(container, values=formas_pagamento, state="readonly", width=28)
    combo_pagamento.grid(row=4, column=1, padx=10, pady=5, sticky="W")

    # Entrada para o valor pago (aparece apenas se a forma de pagamento for dinheiro)
    lbl_valor_pago = ttk.Label(container, text="Valor pago:")
    entry_valor_pago = ttk.Entry(container, width=30)

    def atualizar_valor_pago(event):
        if combo_pagamento.get() == "Dinheiro":
            lbl_valor_pago.grid(row=5, column=0, padx=10, pady=5, sticky="E")
            entry_valor_pago.grid(row=5, column=1, padx=10, pady=5, sticky="W")
        else:
            lbl_valor_pago.grid_remove()
            entry_valor_pago.grid_remove()

    combo_pagamento.bind("<<ComboboxSelected>>", atualizar_valor_pago)

    # Botão para confirmar a compra
    btn_confirmar = ttk.Button(container, text="Confirmar Compra", command=confirmar_compra)
    btn_confirmar.grid(row=6, column=0, columnspan=2, pady=20)

    # Inicia a interface gráfica
    janela.mainloop()

# Iniciar a interface gráfica
iniciar_interface()
