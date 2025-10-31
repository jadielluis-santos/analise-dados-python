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

# 4. Imprimir a tabela inteira
print(df_vendas)