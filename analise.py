import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('vendas_ecommerce.csv', sep=';')

# Converter a coluna 'Data' para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Criar coluna de receita: Preço × Quantidade
df['receita'] = df['Preço'] * df['Quantidade']

# -----------------------
# Análises:
# -----------------------

# 1. Total de pedidos (linhas)
total_pedidos = len(df)
print(f"Total de pedidos: {total_pedidos}")

# 2. Receita total
receita_total = df['receita'].sum()
print(f"Receita total: R$ {receita_total:,.2f}")

# 3. Valor médio por pedido
media_por_pedido = df['receita'].mean()
print(f"Média por pedido: R$ {media_por_pedido:,.2f}")

# 4. Top 5 produtos mais vendidos
mais_vendidos = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 produtos mais vendidos:")
print(mais_vendidos)

# 5. Vendas por categoria
vendas_categoria = df.groupby('Categoria')['Quantidade'].sum()
print("\nVendas por categoria:")
print(vendas_categoria)

# 6. Dia com maior faturamento
dia_maior_receita = df.groupby('Data')['receita'].sum().sort_values(ascending=False).head(1)
print("\nDia com maior faturamento:")
print(dia_maior_receita)

# 7. Receita mês a mês (tendência)
df['Ano_Mes'] = df['Data'].dt.to_period('M')
receita_mensal = df.groupby('Ano_Mes')['receita'].sum()
print("\nReceita por mês:")
print(receita_mensal)
