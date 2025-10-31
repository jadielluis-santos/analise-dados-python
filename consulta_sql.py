import sqlite3

# 1. Conectar ao banco de dados (mesmo arquivo criado antes)
conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

# 2. DEFINIR E EXECUTAR A CONSULTA SQL
# Vamos selecionar o produto, a média de preço e a contagem para cada um.
sql_query = """
SELECT
    Produto,
    AVG(Preco) AS Preco_Medio,
    COUNT(Preco) AS Total_Itens
FROM
    produtos
GROUP BY
    Produto;
"""

cursor.execute(sql_query)
resultados = cursor.fetchall()

# 3. Fechar a conexão
conn.close()

# 4. Imprimir os resultados
print("--- RELATÓRIO SQL: MÉDIA POR PRODUTO ---")
for linha in resultados:
    produto, media, contagem = linha
    print(f"Produto: {produto:<10} | Preço Médio: R${media:.2f} | Qtd: {contagem}")

print("\nConsulta SQL concluída com sucesso!")