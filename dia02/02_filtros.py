# %%
import pandas as pd

# %%
df = pd.read_csv('../data/pedido.csv')

# %%
df.head()

# Filtrar todos as observações cujo estado é São Paulo
# filtro = alguma condição -> exemplo, df['descUF] == 'São Paulo'
# df[filtro]

df[df['descUF'] == 'São Paulo']

# E quem é de São Paulo e flKetchup = True?

filtro = (df['descUF'] == 'São Paulo') & (df['flKetchup'] == True)
df[filtro]

# %%
# E se eu quiser saber quais são todos os estados do dataframe?

df['descUF'].unique()

# %%
# Checando por mais estados sem usar o 'or' ou '|'
# Usando a função .isin() -> funciona como SQL

df['descUF'].isin(['São Paulo', 'Rio de Janeiro', 'Paraná'])
filtro_ufs_ketchup = df['descUF'].isin(['São Paulo', 'Rio de Janeiro', 'Paraná']) & df['flKetchup']
df[filtro_ufs_ketchup]

# %%
# E como eu sei quem não deixou recado? Resposta NaN
# Usando a função .isna() -> checa por NaN

filtro_na = df['txtRecado'].isna()
df[filtro_na]