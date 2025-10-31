# Este é um comentário. O Python o ignora.

# 1. Importar a biblioteca Pandas (O padrão de mercado é chamar de 'pd')
import pandas as pd
import matplotlib.pyplot as plt

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
# 9. VISUALIZAÇÃO DE DADOS (Matplotlib) - Salvando como arquivo

print("\nGerando Gráfico de Barras dos Preços Médios...")

# Cria um gráfico de barras a partir do DataFrame 'media_por_produto'
media_por_produto.plot(kind='bar', title='Preço Médio por Produto')

# Rotaciona os nomes dos produtos no eixo X para melhor visualização
plt.xticks(rotation=0)

# SALVA O GRÁFICO COMO IMAGEM (em vez de usar plt.show())
plt.savefig('media_precos_por_produto.png')

print("Gráfico salvo como 'media_precos_por_produto.png' no diretório.")
# 9. AGRUPAMENTO AVANÇADO: Múltiplas Métricas por Grupo

print("\nRelatório de Métricas Agregadas por Produto:")

# Usamos .agg() para calcular múltiplas estatísticas de uma vez
relatorio_agregado = df_vendas.groupby('Produto')['Preco'].agg(['mean', 'max', 'min', 'count'])

# Renomear as colunas para melhor leitura do relatório
relatorio_agregado.columns = ['Preço Médio', 'Preço Máximo', 'Preço Mínimo', 'Total de Itens']

# Imprimir o relatório completo
print(relatorio_agregado)
# 10. VISUALIZAÇÃO AVANÇADA: Gráfico de Barras com Dados Agrupados

print("\nGerando Gráfico de Barras com Base no Agrupamento:")

# Usamos o DataFrame agrupado que já calculamos anteriormente
# Se você ainda não o tem no mesmo script, use a variável 'media_por_produto' do passo anterior

# Para garantir, vamos recalcular rapidamente a variável de agrupamento para o gráfico:
relatorio_agregado = df_vendas.groupby('Produto')['Preco'].mean() 

# Configuração do Gráfico
relatorio_agregado.plot(
    kind='bar', 
    title='Média de Preço por Produto (Análise SQL via Python)',
    ylabel='Preço Médio (R$)'
)

# Ajustes estéticos
plt.xticks(rotation=45) # Girar os nomes para caberem melhor
plt.tight_layout() # Ajusta margens

# Salva o gráfico
plt.savefig('media_precos_agrupada.png')

print("Gráfico de média por produto salvo como 'media_precos_agrupada.png'")

# Se você ainda quiser ver a janela pop-up (opcionalmente)
# plt.show()