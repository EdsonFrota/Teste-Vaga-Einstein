    # Autor: EDSON JÚNIOR FROTA SILVA
    # DATA: 16/02/2025

import pandas as pd

# Supondo que o arquivo se chame 'vendas.csv'
df = pd.read_csv('vendas.csv')

# Passo 2: Calcular o faturamento total por produto
df['faturamento'] = df['quantidade'] * df['preco_unitario']

# Agrupando por 'produto' e somando o faturamento
faturamento_por_produto = df.groupby('produto')['faturamento'].sum().reset_index()

# Passo 3: Produto com maior e menor faturamento
produto_maior_faturamento = faturamento_por_produto.loc[faturamento_por_produto['faturamento'].idxmax()]
produto_menor_faturamento = faturamento_por_produto.loc[faturamento_por_produto['faturamento'].idxmin()]

# Exibir os resultados
print("Faturamento por produto:")
print(faturamento_por_produto)
print("\nProduto com maior faturamento:")
print(produto_maior_faturamento)
print("\nProduto com menor faturamento:")
print(produto_menor_faturamento)