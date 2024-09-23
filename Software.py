import os

# Criar a pasta data se ainda não existir
os.makedirs('data', exist_ok=True)

# Criar arquivos principais
arquivos = ['main.py', 'agendamentos.py', 'vendas.py', 'clientes.py', 'relatorios.py']
for arquivo in arquivos:
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            f.write(f'# {arquivo} - Módulo criado\n')

print("Estrutura de pastas e arquivos criada com sucesso!")
