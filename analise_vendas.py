# Este é um comentário. O Python o ignora.

# 1. Importar a biblioteca Pandas (O padrão de mercado é chamar de 'pd')
import pandas as pd

# 2. Criar uma série de dados simples (uma lista)
dados = {
    'Produto': ['Camisa', 'Calça', 'Sapato', 'Meia'],
    'Preco': [50.00, 120.00, 85.50, 10.00]
}

# 3. Criar um DataFrame (a tabela de dados do Pandas)
df_vendas = pd.DataFrame(dados)

# 4. Imprimir apenas a coluna 'Preco'
print("\nPreços dos Produtos:")
print(df_vendas['Preco'])

# 5. Imprimir mais de uma coluna (usando uma lista de colunas)
print("\nProduto e Preço:")
print(df_vendas[['Produto', 'Preco']])

# 6. Média de Preço (Primeira análise estatística!)
print("\nMédia de Preços:")
print(df_vendas['Preco'].mean())
