import pandas as pd
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Funções para carregar e salvar agendamentos
def salvar_agendamentos(df):
    df.to_csv('agendamentos.csv', index=False)


def carregar_agendamentos():
    try:
        df = pd.read_csv('agendamentos.csv')
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=['Nome do cliente', 'Serviço', 'Data', 'Hora'])


# Função para adicionar agendamentos
def adicionar_agendamento(nome_cliente, servico, data, hora):
    global df_agendamentos
    novo_agendamento = {'Nome do cliente': nome_cliente, 'Serviço': servico, 'Data': data, 'Hora': hora}
    df_agendamentos = df_agendamentos.append(novo_agendamento, ignore_index=True)
    salvar_agendamentos(df_agendamentos)
    messagebox.showinfo("Sucesso", "Agendamento adicionado com sucesso!")


# Função para editar agendamentos
def editar_agendamento(index, nome_cliente, servico, data, hora):
    global df_agendamentos
    df_agendamentos.at[index, 'Nome do cliente'] = nome_cliente
    df_agendamentos.at[index, 'Serviço'] = servico
    df_agendamentos.at[index, 'Data'] = data
    df_agendamentos.at[index, 'Hora'] = hora
    salvar_agendamentos(df_agendamentos)
    messagebox.showinfo("Sucesso", "Agendamento editado com sucesso!")


# Função para visualizar agendamentos
def visualizar_agendamentos():
    global df_agendamentos
    if df_agendamentos.empty:
        messagebox.showinfo("Informação", "Não há agendamentos para visualizar.")
        return

    visualizacao_janela = tk.Toplevel()
    visualizacao_janela.title("Agendamentos")

    texto = tk.Text(visualizacao_janela)
    for index, row in df_agendamentos.iterrows():
        texto.insert(tk.END, f"{index}: {row['Nome do cliente']} - {row['Serviço']} - {row['Data']} - {row['Hora']}\n")
    texto.pack()


# Função para agendar serviços
def agendar_servicos():
    agendamento_janela = tk.Toplevel()
    agendamento_janela.title("Agendar Serviço")

    tk.Label(agendamento_janela, text="Nome do Cliente").grid(row=0)
    tk.Label(agendamento_janela, text="Serviço").grid(row=1)
    tk.Label(agendamento_janela, text="Data (dd/mm/aaaa)").grid(row=2)
    tk.Label(agendamento_janela, text="Hora").grid(row=3)

    nome_cliente_entry = tk.Entry(agendamento_janela)
    servico_entry = tk.Entry(agendamento_janela)
    data_entry = tk.Entry(agendamento_janela)
    hora_entry = tk.Entry(agendamento_janela)

    nome_cliente_entry.grid(row=0, column=1)
    servico_entry.grid(row=1, column=1)
    data_entry.grid(row=2, column=1)
    hora_entry.grid(row=3, column=1)

    def adicionar():
        adicionar_agendamento(nome_cliente_entry.get(), servico_entry.get(), data_entry.get(), hora_entry.get())
        agendamento_janela.destroy()

    botao_adicionar = tk.Button(agendamento_janela, text="Adicionar", command=adicionar)
    botao_adicionar.grid(row=4, column=1)


# Carregar agendamentos no início
df_agendamentos = carregar_agendamentos()


# Iniciar a interface
def criar_interface():
    root = tk.Tk()
    root.title("Agendamentos")

    frame_menu = tk.Frame(root, bg='lightpink')
    frame_menu.pack(fill=tk.BOTH, expand=True)

    # Botões
    botao_agendar = tk.Button(frame_menu, text="Agendar Serviços", command=agendar_servicos)
    botao_agendar.pack(pady=10)

    botao_visualizar = tk.Button(frame_menu, text="Visualizar Agendamentos", command=visualizar_agendamentos)
    botao_visualizar.pack(pady=10)

    root.mainloop()

    # Salvar agendamentos ao fechar
    salvar_agendamentos(df_agendamentos)


# Iniciar a interface
criar_interface()
