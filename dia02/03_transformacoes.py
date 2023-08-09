# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('../data/produto.csv')

# %%
df.info()
df

# %%
# Criando uma coluna nova

df['precoAjustado'] = round(df['vlPreco'] * 1.09, 2) # ou conforme abaixo
df['precoAjustado'] = (df['vlPreco'] * 1.09).round(2)
df

# %%
df['txAjuste'] = (100 * (df['precoAjustado'] / df['vlPreco'] - 1)).round(2)
df['txAjuste (%)'] = (100 * (df['precoAjustado'] / df['vlPreco'] - 1)).round(2)
df

# %%
# Deletando uma coluna - lembre-se que precisamos atribuir novamente

df = df.drop(columns = 'txAjuste') # mais comum
del df['txAjuste'] # menos comum
df

# %%
# E se quiséssemos aplicar uma função (log, por exemplo) a uma coluna?

df['logtxAjustes'] = np.log(df['txAjuste (%)'])
df['exptxAjuste'] = np.exp(df['txAjuste (%)'])
df

# %%
# E para criar uma função customizada?
# Em primeiro lugar, criamos uma função pensando em apenas um elemento!
# Vamos criar uma função que calcula o fatorial

def fatorial(x):
    total = 1
    for i in range(2, int(x) + 1):
        total *= i
    return total

df['fatprecoAjustado'] = df['precoAjustado'].apply(fatorial)
df