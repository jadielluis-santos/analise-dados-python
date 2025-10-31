import sqlite3

# Dados que serão inseridos (os mesmos que você usou no Pandas)
dados = [
    ('Camisa', 50.00),
    ('Calça', 120.00),
    ('Sapato', 85.50),
    ('Meia', 10.00),
    ('Camisa', 55.00), # Adicionando mais dados para tornar o SQL interessante
    ('Calça', 115.00)  # Adicionando mais dados
]

# 1. Conectar ao banco de dados (Se o arquivo 'vendas.db' não existir, ele será criado)
conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

# 2. Criar a tabela 'produtos' (se ela ainda não existir)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        Produto TEXT,
        Preco REAL
    )
''')

# 3. Inserir os dados na tabela
cursor.executemany('INSERT INTO produtos VALUES (?,?)', dados)

# 4. Salvar (commit) e fechar a conexão
conn.commit()
conn.close()

print("Banco de dados 'vendas.db' criado e populado com sucesso!")