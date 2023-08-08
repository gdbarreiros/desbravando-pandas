# %%
import pandas as pd

# %%
# Isso é um dicionário

data = {
    'nome':[
        'Gabriel',
        'Marcela',
        'Rafaela',
        'Manuela',
        'Valdir',
        'Breno'
    ],
    'idade':[
        28,
        30,
        26,
        10,
        28,
        29
    ],
    'cor':[
        'preto',
        'azul',
        'vermelho',
        'amarelo',
        'verde',
        'rosa'
    ],
    'renda':[
        3500,
        5200,
        4000,
        200,
        4000,
        2000
    ]
}

# %%
# Estrutura de tabela, uma matriz - convertemos o dicionário em um 
# dataframe, numa estrutura tabular

df = pd.DataFrame(data)
df

# Cada coluna de um dataframe é representada por uma Serie!
# O dataframe é um agregador de Series

# dicionario['chave'] -> retorna uma lista
# dataframe['coluna'] -> retorna uma Serie

# São equivalentes, mas o primeiro método é preferível

df['idade']
df.idade

# %%
# Podemos usar as mesmas funções utilizadas em Series, e elas serão 
# aplicadas em todas as colunas aplicáveis

df.mean()
df.var()
df.std()
df.describe()