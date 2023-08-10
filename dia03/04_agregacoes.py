# %%
import pandas as pd
import random

# %%
df_produto = pd.read_csv('../data/produto.csv')
df_produto

# %%
# Tipos de agregações -> sumarizações possíveis de serem aplicados a uma 
# Series do dataframe

df_produto['vlPreco'].sum()
df_produto['vlPreco'].mean()
df_produto['vlPreco'].describe()

# %%
# Também podemos usar o describe() em um dataframe - ele vai considerar 
# todas as colunas numéricas

df_produto['vlPrecoInfla'] = df_produto['vlPreco'] * 1.09
df_produto.describe()

# %%
# E no caso das Series qualitativas?
# Vamos criar uma outra coluna qualitativa primeiro

df_produto['descItemPrimeiro'] = df_produto['descItem'].apply(lambda x: x.split(" ")[0])
df_produto[['descItem', 'descItemPrimeiro']].describe()

# %%
# Tabela de frequência

pd.value_counts(df_produto['descItemPrimeiro'])
pd.value_counts(df_produto['descItemPrimeiro']).plot()

# %%
# Agrupando linhas usando um critério - é preciso definir uma 
# estatística a ser aplicada aos grupos!
# Aqui o valor retornado é um dataframe (caso haja mais de uma
# coluna quantitativa)

df_produto.groupby(by = ['descItemPrimeiro']).mean()

# Calculando a estatística para uma única coluna
# O objeto retornado é uma Series

df_produto.groupby(by = ['descItemPrimeiro'])['vlPreco'].mean()

# %%
df_produto.groupby(by = ['descItemPrimeiro']).describe()

# %%
# Usando o aggregate ou agg para gerar estatísticas descritivas ]
# específicas - não todas as que são apresentadas no describe()

(df_produto.groupby(by = ['descItemPrimeiro'])
            .agg(['mean', 'min', 'max']))

# %%
# E eu posso aplicar uma função própria usando o groupby com o agg
# A única condição é que a função precisa retornar um único valor!

def aleatorio(x):
    return random.choice(x.values)

(df_produto.groupby(by = ['descItemPrimeiro'])
            .agg(['mean', 'min', 'max', aleatorio]))