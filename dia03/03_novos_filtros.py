# %%
import pandas as pd
pd.set_option('display.max_rows', 100)

# %%
df_produto = pd.read_csv('../data/produto.csv')
df_produto

# %%
# Criando uma nova coluna com o primeiro nome de cada linha
# Estamos fazendo isso apenas para simular dados repetidos/duplicados

df_produto['descItem'].apply(lambda x: x.split(" ")[0])

# Atribuindo a uma nova coluna

df_produto['primeiroNome'] = df_produto['descItem'].apply(lambda x: x.lower().split(" ")[0])
df_produto

# %%
# E como fazemos para tratar os dados duplicados?
# O primeiro caso, é comparar linhas inteiras

df_produto.drop_duplicates() # aqui ele não apaga nada

# No entanto, podemos remover colunas com base em um subset (ou coluna)

df_produto.drop_duplicates(subset = ['primeiroNome']) # nesse caso, ele 
                                                      # mantém só a 1ª
                                                      # ocorrência - na 
                                                      # ordem em que está
                                                      # o dataframe

# %%
# Vamos trabalhar com os dados de pedidos agora

df_pedidos = pd.read_csv('../data/pedido.csv')
df_pedidos

# %%
# Remover todas as linhhas que contém ao menos uma coluna com NaN

df_pedidos.dropna()

# Para excluir apenas linhas que contém todos os valores NaN (todas as
# colunas)

df_pedidos.dropna(how = 'all')

# Para remover os NaN apenas de uma coluna específica, devemos usar
# o subset

df_pedidos.dropna(subset = 'txtRecado')