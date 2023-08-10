# %%
import pandas as pd

# Visualizar um número máximo de linhas

pd.set_option('display.max_rows', 500)

# %%
df_produto = pd.read_csv('../data/produto.csv')
df_produto

# %%
# Ordenando por um único critério

df_produto.sort_values(by = 'vlPreco', ascending = False)

# %%
# Ordenando por mais de um critério

df_produto.sort_values(by = ['vlPreco', 'descItem'], ascending = [False, True])