from faker import Faker
import pandas as pd 
from datetime import datetime, timedelta
import random

fake = Faker('pt_BR')

produtos = [
    ('headset', 'Eletrônicos', 199.99),
    ('camiseta oversized','Moda', 89.99),
    ('pc gamer','Eletrônicos', 3499.99),
    ('Tênis','Calçados', 189.99),
    ('notebook','Eletrônicos', 1499.99),
        ]    

formas_pagamento = ['Cartão de Crédito', 'Cartão Débito', 'Boleto', 'Pix']

dados = []

for i in range(100): #número de registros
    nome = fake.name()
    id_cliente = f"C{str(i+1).zfill(3)}"
    produto, categoria, preco = random.choice(produtos)
    quantidade = random.randint(1, 3)
    pagamento = random.choice(formas_pagamento)
    cidade = fake.city()
    data = fake.date_between(start_date="-6M", end_date='today')

    dados.append([data, id_cliente, nome, produto, categoria, preco, quantidade, pagamento, cidade])

colunas = ['Data', 'ID_Cliente', 'Nome_Cliente', 'Produto', 'Categoria', 'Preço', 'Quantidade', 'Pagamento', 'Cidade']

df = pd.DataFrame(dados, columns=colunas)
df.to_csv('vendas_ecommerce.csv', sep=';', index=False)