# Módulo de Análise de Dados: Python, Pandas e Matplotlib

# 1. IMPORTAÇÕES
import pandas as pd
import matplotlib.pyplot as plt

# 2. DADOS DE ENTRADA
dados = {
    'Produto': ['Camisa', 'Calça', 'Sapato', 'Meia'],
    'Preco': [50.00, 120.00, 85.50, 10.00]
}

# 3. CRIAÇÃO DO DATAFRAME
df_vendas = pd.DataFrame(dados)

# ==========================================================
# 4. ANÁLISE BÁSICA E FILTRAGEM
# ==========================================================

print("--- 1. ANÁLISE ESTATÍSTICA BÁSICA ---")

# Seleção de Coluna Única e Média
print(f"Média de Preços Total: R${df_vendas['Preco'].mean():.2f}")

# Filtro Condicional (Preços > R$80.00)
preco_alto = df_vendas['Preco'] > 80.00
df_filtrado = df_vendas[preco_alto]
print("\nProdutos com Preço Superior a R$80.00:")
print(df_filtrado)


# ==========================================================
# 5. AGRUPAMENTO AVANÇADO (Relatório de BI)
# ==========================================================

print("\n--- 2. RELATÓRIO DE MÉTRICAS POR PRODUTO (.groupby().agg()) ---")

# Calculamos múltiplas estatísticas para o relatório
relatorio_agregado = df_vendas.groupby('Produto')['Preco'].agg(['mean', 'max', 'min', 'count'])
relatorio_agregado.columns = ['Preço Médio', 'Preço Máximo', 'Preço Mínimo', 'Total de Itens']

# Imprimir o relatório
print(relatorio_agregado)


# ==========================================================
# 6. VISUALIZAÇÃO DE DADOS (Matplotlib)
# ==========================================================

print("\n--- 3. VISUALIZAÇÕES SALVAS NO DIRETÓRIO ---")

# 6.1 GRÁFICO 1: Média Simples (Como a última análise feita)
plt.figure(figsize=(7, 5)) # Define o tamanho do gráfico
relatorio_agregado['Preço Médio'].plot(kind='bar', title='Média de Preço por Produto')
plt.xticks(rotation=0)
plt.ylabel('Preço Médio (R$)')
plt.tight_layout()
plt.savefig('media_precos_agrupada.png')
print("Gráfico 'media_precos_agrupada.png' salvo com sucesso.")


# 6.2 GRÁFICO 2: Contagem de Itens
plt.figure(figsize=(7, 5)) 
relatorio_agregado['Total de Itens'].plot(kind='bar', title='Total de Itens Vendidos (Contagem)')
plt.xticks(rotation=0)
plt.ylabel('Contagem')
plt.tight_layout()
plt.savefig('contagem_itens_vendidos.png')
print("Gráfico 'contagem_itens_vendidos.png' salvo com sucesso.")