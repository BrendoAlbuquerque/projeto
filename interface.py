import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
import os
import matplotlib.pyplot as plt

# Carregar agendamentos
def carregar_agendamentos():
    try:
        df = pd.read_csv('.venv/agendamentos.csv')
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=['Nome do cliente', 'Serviço', 'Data', 'Hora', 'Preço'])

# Salvar agendamentos
def salvar_agendamentos(df):
    df.to_csv('agendamentos.csv', index=False)

# Criar backup de agendamentos
def criar_backup():
    if os.path.exists('.venv/agendamentos.csv'):
        backup_df = pd.read_csv('.venv/agendamentos.csv')
        backup_df.to_csv('backup_agendamentos.csv', index=False)

# Função para gerar relatório
def gerar_relatorio():
    global df_agendamentos
    if df_agendamentos.empty:
        messagebox.showinfo("Informação", "Não há agendamentos para gerar relatório.")
        return

    relatorio_janela = tk.Toplevel()
    relatorio_janela.title("Análise de Tendências de Atendimento e Preferências")

    relatorio_texto = tk.Text(relatorio_janela, wrap=tk.WORD)
    relatorio_texto.pack(expand=True, fill='both')

    tend_df = df_agendamentos.groupby(['Data', 'Serviço']).size().reset_index(name='Quantidade')
    tend_df = tend_df.sort_values(by=['Data', 'Quantidade'], ascending=[True, False])

    for index, row in tend_df.iterrows():
        relatorio_texto.insert(tk.END,
                               f"Data: {row['Data']} - Serviço: {row['Serviço']} - Quantidade: {row['Quantidade']}\n")

# Função para agendar serviços
def agendar_servicos():
    agendamento_janela = tk.Toplevel()
    agendamento_janela.title("Agendar Serviço")
    agendamento_janela.configure(bg='lightblue')

    tk.Label(agendamento_janela, text="Nome do Cliente", bg='lightblue').grid(row=0)
    tk.Label(agendamento_janela, text="Serviço", bg='lightblue').grid(row=1)
    tk.Label(agendamento_janela, text="Data (dd/mm/aaaa)", bg='lightblue').grid(row=2)
    tk.Label(agendamento_janela, text="Hora", bg='lightblue').grid(row=3)
    tk.Label(agendamento_janela, text="Preço", bg='lightblue').grid(row=4)

    nome_cliente_entry = tk.Entry(agendamento_janela)
    servico_var = tk.StringVar()
    servico_dropdown = tk.OptionMenu(agendamento_janela, servico_var, "Corte Masculino", "Corte Feminino", "Escova", "Manicure", "Alisamento", "Progressiva", "Depilação", "Sobrancelha")
    data_entry = tk.Entry(agendamento_janela)
    hora_entry = tk.Entry(agendamento_janela)
    preco_entry = tk.Entry(agendamento_janela)

    nome_cliente_entry.grid(row=0, column=1)
    servico_dropdown.grid(row=1, column=1)
    data_entry.grid(row=2, column=1)
    hora_entry.grid(row=3, column=1)
    preco_entry.grid(row=4, column=1)

    def adicionar():
        nome_cliente = nome_cliente_entry.get()
        servico = servico_var.get()
        data = data_entry.get()
        hora = hora_entry.get()
        preco = preco_entry.get()

        if nome_cliente and servico and data and hora and preco:
            novo_agendamento = {'Nome do cliente': nome_cliente, 'Serviço': servico, 'Data': data, 'Hora': hora,
                                'Preço': preco}
            global df_agendamentos
            df_agendamentos = pd.concat([df_agendamentos, pd.DataFrame([novo_agendamento])], ignore_index=True)
            salvar_agendamentos(df_agendamentos)
            messagebox.showinfo("Sucesso", "Agendamento adicionado com sucesso!")
            agendamento_janela.destroy()
        else:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")

    botao_adicionar = tk.Button(agendamento_janela, text="Adicionar", command=adicionar, bg='lightgreen')
    botao_adicionar.grid(row=5, column=1)


# Função para editar agendamentos
def editar_agendamentos():
    global df_agendamentos
    if df_agendamentos.empty:
        messagebox.showinfo("Informação", "Não há agendamentos para editar.")
        return

    editar_janela = tk.Toplevel()
    editar_janela.title("Editar Agendamentos")
    editar_janela.configure(bg='lightblue')

    tk.Label(editar_janela, text="Selecione o índice do agendamento para editar", bg='lightblue').grid(row=0)

    lista_agendamentos = tk.Listbox(editar_janela)
    for index, row in df_agendamentos.iterrows():
        lista_agendamentos.insert(tk.END,
                                  f"{index}: {row['Nome do cliente']} - {row['Serviço']} - {row['Data']} - {row['Hora']} - Preço: {row['Preço']}")
    lista_agendamentos.grid(row=1, columnspan=2)

    def carregar_agendamento():
        try:
            selecionado = lista_agendamentos.curselection()[0]
            agendamento = df_agendamentos.iloc[selecionado]

            nome_cliente_entry.delete(0, tk.END)
            servico_var.set(agendamento['Serviço'])
            data_entry.delete(0, tk.END)
            hora_entry.delete(0, tk.END)
            preco_entry.delete(0, tk.END)

            nome_cliente_entry.insert(0, agendamento['Nome do cliente'])
            data_entry.insert(0, agendamento['Data'])
            hora_entry.insert(0, agendamento['Hora'])
            preco_entry.insert(0, agendamento['Preço'])
        except IndexError:
            messagebox.showwarning("Selecione", "Selecione um agendamento para editar.")

    # Campos de entrada para edição
    tk.Label(editar_janela, text="Nome do Cliente", bg='lightblue').grid(row=2)
    tk.Label(editar_janela, text="Serviço", bg='lightblue').grid(row=3)
    tk.Label(editar_janela, text="Data", bg='lightblue').grid(row=4)
    tk.Label(editar_janela, text="Hora", bg='lightblue').grid(row=5)
    tk.Label(editar_janela, text="Preço", bg='lightblue').grid(row=6)

    nome_cliente_entry = tk.Entry(editar_janela)
    servico_var = tk.StringVar()
    servico_dropdown = tk.OptionMenu(editar_janela, servico_var, "Corte Masculino", "Corte Feminino", "Escova", "Manicure", "Alisamento", "Progressiva", "Depilação", "Sobrancelha")
    data_entry = tk.Entry(editar_janela)
    hora_entry = tk.Entry(editar_janela)
    preco_entry = tk.Entry(editar_janela)

    nome_cliente_entry.grid(row=2, column=1)
    servico_dropdown.grid(row=3, column=1)
    data_entry.grid(row=4, column=1)
    hora_entry.grid(row=5, column=1)
    preco_entry.grid(row=6, column=1)

    botao_carregar = tk.Button(editar_janela, text="Carregar", command=carregar_agendamento, bg='lightgreen')
    botao_carregar.grid(row=1, column=2)

    def salvar_edicao():
        try:
            selecionado = lista_agendamentos.curselection()[0]
            df_agendamentos.at[selecionado, 'Nome do cliente'] = nome_cliente_entry.get()
            df_agendamentos.at[selecionado, 'Serviço'] = servico_var.get()
            df_agendamentos.at[selecionado, 'Data'] = data_entry.get()
            df_agendamentos.at[selecionado, 'Hora'] = hora_entry.get()
            df_agendamentos.at[selecionado, 'Preço'] = preco_entry.get()
            salvar_agendamentos(df_agendamentos)
            messagebox.showinfo("Sucesso", "Agendamento editado com sucesso!")
            editar_janela.destroy()
        except IndexError:
            messagebox.showwarning("Selecione", "Selecione um agendamento para editar.")

    botao_salvar = tk.Button(editar_janela, text="Salvar Edição", command=salvar_edicao, bg='lightgreen')
    botao_salvar.grid(row=7, column=1)

# Função para pesquisar agendamentos
def pesquisar_agendamentos():
    pesquisa_janela = tk.Toplevel()
    pesquisa_janela.title("Pesquisar Agendamentos")
    pesquisa_janela.configure(bg='lightblue')

    tk.Label(pesquisa_janela, text="Digite o nome do cliente:", bg='lightblue').grid(row=0)
    pesquisa_entry = tk.Entry(pesquisa_janela)
    pesquisa_entry.grid(row=0, column=1)

    resultados_texto = tk.Text(pesquisa_janela, wrap=tk.WORD)
    resultados_texto.grid(row=1, columnspan=2)

    def buscar():
        nome_cliente = pesquisa_entry.get()
        resultados_texto.delete(1.0, tk.END)
        resultados = df_agendamentos[df_agendamentos['Nome do cliente'].str.contains(nome_cliente, na=False)]
        if resultados.empty:
            resultados_texto.insert(tk.END, "Nenhum agendamento encontrado.")
        else:
            for index, row in resultados.iterrows():
                resultados_texto.insert(tk.END,
                                         f"{index}: {row['Nome do cliente']} - {row['Serviço']} - {row['Data']} - {row['Hora']} - Preço: {row['Preço']}\n")

    botao_buscar = tk.Button(pesquisa_janela, text="Buscar", command=buscar, bg='lightgreen')
    botao_buscar.grid(row=0, column=2)

# Função para gerar relatórios avançados
def relatorio_avancado():
    global df_agendamentos
    if df_agendamentos.empty:
        messagebox.showinfo("Informação", "Não há agendamentos para gerar relatório.")
        return

    servicos_count = df_agendamentos['Serviço'].value_counts()
    plt.figure(figsize=(10, 6))
    servicos_count.plot(kind='bar', color='lightblue')
    plt.title("Serviços Mais Solicitados")
    plt.xlabel("Serviços")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Criar a interface principal
def criar_interface():
    global df_agendamentos
    df_agendamentos = carregar_agendamentos()

    root = tk.Tk()
    root.title("Sistema de Agendamento")
    root.configure(bg='lightblue')

    frame_menu = tk.Frame(root, bg='lightblue')
    frame_menu.pack(pady=20)

    botao_agendar = tk.Button(frame_menu, text="Agendar Serviços", command=agendar_servicos, bg='lightgreen')
    botao_agendar.pack(side=tk.LEFT, padx=10)

    botao_editar = tk.Button(frame_menu, text="Editar Agendamentos", command=editar_agendamentos, bg='lightgreen')
    botao_editar.pack(side=tk.LEFT, padx=10)

    botao_pesquisar = tk.Button(frame_menu, text="Pesquisar Agendamentos", command=pesquisar_agendamentos, bg='lightgreen')
    botao_pesquisar.pack(side=tk.LEFT, padx=10)

    botao_relatorio = tk.Button(frame_menu, text="Relatório", command=gerar_relatorio, bg='lightgreen')
    botao_relatorio.pack(side=tk.LEFT, padx=10)

    botao_relatorio_avancado = tk.Button(frame_menu, text="Relatório Avançado", command=relatorio_avancado, bg='lightgreen')
    botao_relatorio_avancado.pack(side=tk.LEFT, padx=10)

    botao_backup = tk.Button(frame_menu, text="Criar Backup", command=criar_backup, bg='lightgreen')
    botao_backup.pack(side=tk.LEFT, padx=10)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()

