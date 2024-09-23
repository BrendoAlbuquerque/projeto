import pandas as pd

CAMINHO_ARQUIVO_CLIENTES = 'data/clientes.csv'


def inicializar_arquivo_clientes():
    """Inicializa o arquivo CSV com um cabeçalho se ele não existir."""
    try:
        df = pd.read_csv(CAMINHO_ARQUIVO_CLIENTES)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['ID', 'Nome', 'Telefone', 'Email'])
        df.to_csv(CAMINHO_ARQUIVO_CLIENTES, index=False)


def adicionar_cliente(id_cliente, nome, telefone, email):
    """Adiciona um cliente ao arquivo CSV."""
    try:
        df = pd.read_csv(CAMINHO_ARQUIVO_CLIENTES)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['ID', 'Nome', 'Telefone', 'Email'])

    novo_cliente = pd.DataFrame([[id_cliente, nome, telefone, email]], columns=['ID', 'Nome', 'Telefone', 'Email'])
    df = pd.concat([df, novo_cliente], ignore_index=True)
    df.to_csv(CAMINHO_ARQUIVO_CLIENTES, index=False)


def listar_clientes():
    """Lista todos os clientes do arquivo CSV."""
    try:
        df = pd.read_csv(CAMINHO_ARQUIVO_CLIENTES)
        if df.empty:
            print("Nenhum cliente encontrado.")
        else:
            print(df.to_string(index=False))
    except FileNotFoundError:
        print("Nenhum cliente encontrado.")


def buscar_cliente(nome):
    """Busca um cliente pelo nome no arquivo CSV."""
    try:
        df = pd.read_csv(CAMINHO_ARQUIVO_CLIENTES)
        resultados = df[df['Nome'].str.contains(nome, case=False, na=False)]
        if resultados.empty:
            print("Nenhum cliente encontrado.")
        else:
            print(resultados.to_string(index=False))
    except FileNotFoundError:
        print("Nenhum cliente encontrado.")


# Testes
if __name__ == "__main__":
    inicializar_arquivo_clientes()  # Garante que o arquivo de clientes existe

    # Adiciona alguns clientes
    adicionar_cliente(1, 'Brendo Albuquerque', '123456789', 'brendo@example.com')
    adicionar_cliente(2, 'Ana Silva', '987654321', 'ana@example.com')

    # Lista todos os clientes
    print("Clientes cadastrados:")
    listar_clientes()

    # Busca um cliente
    print("\nBuscando cliente 'Brendo':")
    buscar_cliente('Brendo')
