import pandas as pd
import matplotlib
matplotlib.use('Agg')  # usar backend sem GUI
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('vendas_ecommerce.csv', sep=';', parse_dates=['Data'])
print(df.head())
print(df.columns)
 


# Já carregou seu DataFrame df

# Exemplo: Gráfico de barras dos Top 5 produtos mais vendidos
top5_produtos = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(8,5))
sns.barplot(x=top5_produtos.index, y=top5_produtos.values, palette='viridis')
plt.title('Top 5 Produtos Mais Vendidos')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Exemplo: Receita por mês (linha)
df['receita'] = df['Preço'] * df['Quantidade']  # nova coluna receita
df['Ano_Mes'] = df['Data'].dt.to_period('M')
receita_mensal = df.groupby('Ano_Mes')['receita'].sum()

plt.figure(figsize=(10,6))
receita_mensal.index = receita_mensal.index.astype(str)
sns.lineplot(x=receita_mensal.index, y=receita_mensal.values, marker='o')
plt.title('Receita Mensal')
plt.xlabel('Mês')
plt.ylabel('Receita (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_receita_mensal.png")  # salva o gráfico
# plt.show()  # desnecessário se estiver em modo sem interface gráfica
