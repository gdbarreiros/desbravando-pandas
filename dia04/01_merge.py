# %%
import pandas as pd

# %%
df_item_pedido = pd.read_csv('../data/item_pedido.csv')

df_produto = pd.read_csv('../data/produto.csv')

df_pedido = pd.read_csv('../data/pedido.csv')

# %%
# Vamos unir as duas tabelas importadas usando o merge
# Se temos colunas iguais nas duas tabelas, não precisamos indicar nada na 
# chamada do merge

df_item_pedido.merge(df_produto, how = 'left')

# %%
# Mas se quiséssemos especificar as colunas, bastaria fazer

df_item_pedido.merge(df_produto, how = 'left', on = ['descItem'])

# E o resultado seria o mesmo

# %%
# Vamos renomear uma das colunas e ver o que acontece

df_item_pedido = df_item_pedido.rename(columns = {'descItem': 'descProduto'})

# Isso vai gerar um erro

df_item_pedido.merge(df_produto, how = 'left')

# Podemos resolver isso fazendo

df_item_pedido.merge(right = df_produto, 
                     how = 'left', 
                     left_on = ['descItem'], 
                     right_on = ['descProduto'],
                     )

# %%
# Merge na sequência de outro merge

df_join = df_item_pedido.merge(df_produto, how = 'left', on = ['descItem'])
df_join.merge(df_pedido, how = 'left')

# Também poderíamos fazer

df_join = (df_item_pedido.merge(df_produto, how = 'left')
                         .merge(df_pedido, how = 'left'))
df_join