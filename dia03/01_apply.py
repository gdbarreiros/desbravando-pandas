# %%
import pandas as pd

# %%
df_produto = pd.read_csv('../data/produto.csv')
df_produto

# %% 
def is_massa(x):
    return x.lower().startswith('massa')

# %%
# Aplicando a função a coluna descItem do dataframe

df_produto['descItem'].apply(is_massa)

# %%
# Criando um filtro usando o apply

filtro_massa = df_produto['descItem'].apply(is_massa)
df_produto[filtro_massa]

# %%
# Funções anônimas -> funções lambda
# Criando uma função sem defini-la

df_produto['descItem'].apply(lambda x: x.lower().startswith('massa'))

# O 'x' representa cada um dos valores da série

# %%
# Usando o str para utilizar os métodos do tipo de variável string

df_produto['descItem'].str.lower().str.startswith('massa')