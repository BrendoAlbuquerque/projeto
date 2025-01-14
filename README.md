# Sistema de Agendamento para Salões de Beleza

Este projeto é parte de uma atividade de extensão da faculdade e tem como objetivo desenvolver um software para gerenciar agendamentos de serviços em salões de beleza. O sistema permite que usuários agendem, editem e visualizem compromissos, além de gerar relatórios com análises de tendências de atendimento.

## Funcionalidades

- Agendamento de serviços (corte, escova, manicure, etc.).
- Edição e exclusão de compromissos.
- Visualização dos compromissos agendados.
- Geração de relatórios com análise dos horários, serviços e dias mais solicitados.
- Backup automático dos agendamentos.
- Interface gráfica intuitiva com esquema de cores customizado.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Tkinter**: Para a construção da interface gráfica.
- **Pandas**: Para manipulação de dados.
- **Matplotlib**: Para geração de gráficos nos relatórios.
- **SQLite**: Banco de dados para armazenamento dos agendamentos.

## Requisitos de Instalação

Certifique-se de ter o Python instalado. Para instalar as dependências do projeto, use o arquivo `requirements.txt`:

```bash
$ pip install -r requirements.txt

$ python interface.py
