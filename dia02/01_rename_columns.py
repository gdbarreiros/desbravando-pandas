# %%
import pandas as pd

# %%
df = pd.read_csv('../data/pedido.csv')

# %%
# Renomeando as colunas do dataframe
# Passamos um dicionário para o parâmetro columns, com a chave -> nome antigo da coluna
# valor -> nome novo da coluna

df.rename(columns = {'descUF':'descEstado'})

# Para salvar o nome dataframe, você tem que atribui-lo a uma variável
# Maneira 1 - mais usual

df = df.rename(columns = {'descUF':'descEstado'})

# Maneira 2 - menos usual

df.rename(columns = {'descUF':'descEstado'}, inplace = True)