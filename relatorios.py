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


# Função para gerar relatórios
def gerar_relatorio():
    df_agendamentos = carregar_agendamentos()

    if df_agendamentos.empty:
        messagebox.showinfo("Informação", "Não há agendamentos para gerar relatórios.")
        return

    # Processar dados para o relatório
    df_agendamentos['Data'] = pd.to_datetime(df_agendamentos['Data'], format='%d/%m/%Y')

    # Contagem de serviços agendados
    relatorio_servicos = df_agendamentos['Serviço'].value_counts()
    relatorio_horas = df_agendamentos['Hora'].value_counts()
    relatorio_dias = df_agendamentos['Data'].dt.day_name().value_counts()

    # Criação do relatório
    relatorio_texto = "Ranking de Serviços Solicitados:\n"
    relatorio_texto += relatorio_servicos.to_string() + "\n\n"
    relatorio_texto += "Horários Agendados:\n"
    relatorio_texto += relatorio_horas.to_string() + "\n\n"
    relatorio_texto += "Dias mais Agendados:\n"
    relatorio_texto += relatorio_dias.to_string()

    # Exibir relatório em uma nova janela
    relatorio_janela = tk.Toplevel()
    relatorio_janela.title("Relatório de Agendamentos")
    relatorio_texto_widget = tk.Text(relatorio_janela, wrap=tk.WORD)
    relatorio_texto_widget.insert(tk.END, relatorio_texto)
    relatorio_texto_widget.pack(expand=True, fill=tk.BOTH)
    relatorio_texto_widget.config(state=tk.DISABLED)


# Função para agendar serviços
def agendar_servicos():
    # Lógica para agendar serviços
    pass


# Função para visualizar vendas
def visualizar_vendas():
    # Lógica para visualizar vendas
    pass


# Interface Gráfica
def criar_interface():
    root = tk.Tk()
    root.title("Agendamentos")

    frame_menu = tk.Frame(root, bg='lightpink')
    frame_menu.pack(fill=tk.BOTH, expand=True)

    # Carregar agendamentos
    df_agendamentos = carregar_agendamentos()

    # Botões
    botao_agendar = tk.Button(frame_menu, text="Agendar Serviços", command=agendar_servicos)
    botao_agendar.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    botao_visualizar = tk.Button(frame_menu, text="Visualizar Vendas", command=visualizar_vendas)
    botao_visualizar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    botao_relatorio = tk.Button(frame_menu, text="Gerar Relatório", command=gerar_relatorio)
    botao_relatorio.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

    root.mainloop()

    # Salvar agendamentos ao fechar
    salvar_agendamentos(df_agendamentos)


# Iniciar a interface
criar_interface()
