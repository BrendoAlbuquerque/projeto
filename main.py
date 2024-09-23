import pandas as pd

ARQUIVO_AGENDAMENTOS = 'agendamentos.csv'

def carregar_agendamentos():
    try:
        return pd.read_csv(ARQUIVO_AGENDAMENTOS)
    except FileNotFoundError:
        print("Arquivo de agendamentos não encontrado. Criando um novo arquivo.")
        return pd.DataFrame(columns=['Nome do cliente', 'Serviço', 'Data', 'Hora'])
    except pd.errors.EmptyDataError:
        print("O arquivo de agendamentos está vazio. Criando um novo arquivo.")
        return pd.DataFrame(columns=['Nome do cliente', 'Serviço', 'Data', 'Hora'])
    except pd.errors.ParserError:
        print("Erro ao ler o arquivo de agendamentos. Verifique o formato.")
        return pd.DataFrame(columns=['Nome do cliente', 'Serviço', 'Data', 'Hora'])

def salvar_agendamentos(df):
    df.to_csv(ARQUIVO_AGENDAMENTOS, index=False)

def adicionar_agendamento(df):
    print("\nAdicionando novo agendamento...")
    nome_cliente = input("Nome do cliente: ")
    servico = input("Serviço: ")
    data = input("Data (dd/mm/aaaa): ")
    hora = input("Hora (hh:mm): ")

    novo_agendamento = {
        'Nome do cliente': nome_cliente,
        'Serviço': servico,
        'Data': data,
        'Hora': hora
    }

    novo_agendamento_df = pd.DataFrame([novo_agendamento])
    df = pd.concat([df, novo_agendamento_df], ignore_index=True)

    salvar_agendamentos(df)
    print("Agendamento adicionado com sucesso.")
    return df

def visualizar_vendas(df):
    print("\nAgendamentos:")
    print(df)

def editar_agendamento(df):
    print("\nEditando agendamento...")
    nome_cliente = input("Nome do cliente do agendamento a ser editado: ")

    agendamento = df[df['Nome do cliente'] == nome_cliente]
    if agendamento.empty:
        print("Nenhum agendamento encontrado para o cliente.")
        return df

    print(f"Agendamentos encontrados para {nome_cliente}:")
    print(agendamento)

    while True:
        try:
            index = int(input("Digite o índice do agendamento a ser editado: "))
            if index < 0 or index >= len(df):
                print("Índice inválido. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    novo_servico = input("Novo serviço: ")
    nova_data = input("Nova data (dd/mm/aaaa): ")
    nova_hora = input("Nova hora (hh:mm): ")

    df.loc[index, 'Serviço'] = novo_servico
    df.loc[index, 'Data'] = nova_data
    df.loc[index, 'Hora'] = nova_hora

    salvar_agendamentos(df)
    print("Agendamento atualizado com sucesso.")
    return df

def excluir_agendamento(df):
    print("\nExcluindo agendamento...")
    nome_cliente = input("Nome do cliente do agendamento a ser excluído: ")

    if nome_cliente not in df['Nome do cliente'].values:
        print("Nenhum agendamento encontrado para o cliente.")
        return df

    df = df[df['Nome do cliente'] != nome_cliente]
    salvar_agendamentos(df)
    print("Agendamento excluído com sucesso.")
    return df

def gerar_relatorios():
    print("\nGerar relatórios - funcionalidade ainda não implementada.")

def gerenciar_clientes():
    print("\nGerenciamento de Clientes")
    print("1. Adicionar Cliente")
    print("2. Visualizar Clientes")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_cliente()
    elif opcao == '2':
        visualizar_clientes()
    else:
        print("Opção inválida.")

def adicionar_cliente():
    print("\nAdicionando novo cliente...")
    nome_cliente = input("Nome do cliente: ")
    contato = input("Contato: ")

    # Adicionando o cliente em um arquivo ou banco de dados (não implementado aqui)
    print("Cliente adicionado com sucesso.")

def visualizar_clientes():
    print("\nVisualizar clientes - funcionalidade ainda não implementada.")

def main():
    df_agendamentos = carregar_agendamentos()

    while True:
        print("\nMenu:")
        print("1. Agendar Serviços")
        print("2. Visualizar Vendas")
        print("3. Gerar Relatórios")
        print("4. Gerenciar Clientes")
        print("5. Editar Agendamentos")
        print("6. Excluir Agendamentos")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            df_agendamentos = adicionar_agendamento(df_agendamentos)
        elif opcao == '2':
            visualizar_vendas(df_agendamentos)
        elif opcao == '3':
            gerar_relatorios()
        elif opcao == '4':
            gerenciar_clientes()
        elif opcao == '5':
            df_agendamentos = editar_agendamento(df_agendamentos)
        elif opcao == '6':
            df_agendamentos = excluir_agendamento(df_agendamentos)
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
