# %%
import pandas as pd

# %%
# Isso é uma lista, mas ela não é performática
# E também não tem por finalidade fins analíticos - outras estruturas 
# são mais recomendadas

idade = [31, 33, 2, 29, 60, 58, 31, 45, 24]
type(idade)

# Series do pandas - semelhante a uma lista que também possui índices

s_idade = pd.Series(idade)
s_idade

# %%
# No caso das Series do pandas, todos os elementos precisam ser 
# do mesmo tipo (str, int, float, etc)

media = s_idade.mean()
variancia = s_idade.var()
desv_pad = s_idade.std()
s_idade.describe()

# %%
# For é pouco performático, prefira vetores!

filtro = s_idade >= 30
s_idade[filtro]

# Que é equivalente 

s_idade[s_idade >= 30]