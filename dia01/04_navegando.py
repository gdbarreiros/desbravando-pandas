# %% 
import pandas as pd

# %%
df = pd.read_csv('../data/pedido.csv')
df

# %%

# Como fazemos pra navegar nas linhas e colunas do nosso dataframe
# Acessar uma coluna -> mesma sintaxe do dicionário

df[['idPedido', 'flKetchup']]

# Reorganizar o dataframe
# Isso não modifica o dataframe!

colunas = [
    'idPedido',
    'descUF',
    'flKetchup',
    'txtRecado',
    'dtPedido'
]

df[colunas]

# Para modifica-lo, temos que fazer

df = df[colunas]

# %%
# E para navegarmos nas linhas?
# Vamos trabalhar com um sample, pra começar

df_sample = df.sample(100)

# %%
# iloc
# Retornando a linha cuja posição é 0 (não é do índice!)
# Retornando a primeira linha

# iloc -> integer location

df_sample.iloc[0] # aqui, o pandas também retorna uma Serie

# Definindo um range (ou uma lista de posições)

df_sample.iloc[0:5]

# %%
# loc
# Retornando observações pelo índice!

df_sample.loc[388]

# Como estamos trabalhando com um sample, os índices estão embaralhados, 
# então o slice (provavelmente) não vai funcionar

# O slice no loc precisa ser completamente satisfeito, caso contrário ele
# não retorna nada