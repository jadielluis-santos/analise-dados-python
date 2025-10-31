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
# 7. FILTROS CONDICIONAIS
print("\nProdutos com Preço Superior a R$80.00:")

# Cria uma "Máscara" Booleana (True/False)
# A variável 'preco_alto' será True para preços > 80.00 e False para o restante
preco_alto = df_vendas['Preco'] > 80.00

# Aplica a máscara ao DataFrame original para mostrar apenas as linhas True
df_filtrado = df_vendas[preco_alto]

# Imprime o novo DataFrame filtrado
print(df_filtrado)
# 8. AGRUPAMENTO DE DADOS COM .groupby()

# Objetivo: Calcular a média de Preço por Produto.
print("\nPreço Médio por Produto (Agrupamento):")

# 1. Agrupar o DataFrame pela coluna 'Produto'
df_agrupado = df_vendas.groupby('Produto')

# 2. Aplicar a função de média (.mean()) à coluna 'Preco' dentro de cada grupo
media_por_produto = df_agrupado['Preco'].mean()

# 3. Imprimir o resultado
print(media_por_produto)