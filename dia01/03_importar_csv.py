# %%
import pandas as pd

# %%    

df = pd.read_csv('../data/pedido.csv')
df

# %%

# Acessando as colunas

df.columns

# Acessando as dimensões, tal qual uma matriz - (linhas, colunas)

df.shape

# Informações detalhadas sobre o dataframe

df.info(memory_usage='deep') # usamos o deep para termos
                             # maior precissão em termos de uso da 
                             # memória

# Tipos das colunas - o valor retornado é uma Serie!
df.dtypes

# Primeiras linhas - 5 linhas é o default

df.head()

# Últimas linhas - 5 linhas é o default

df.tail()

# Dados aletórios - 1 linha é o default

df.sample() 