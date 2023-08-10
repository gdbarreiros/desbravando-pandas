# %%
import pandas as pd

# %%
df_mods = pd.DataFrame({'nome':['Kozato0', 'Sky', 'Nah', 'Karlla'],
                       'idade':[30, 34, 28, 27]})

df_subs = pd.DataFrame({'nome':['Sky', 'Mari', 'Bel', 'Maltrapilho', 'Mathes'],
                        'idade':[34, 30, 29, 35, 26],
                        'meses_subs':[24, 1, 1, 6, 1]})

# %%
# O concat é usado para empilhar dataframes
# Ele recebe uma lista com os dataframes a serem 
# concatenados

(pd.concat([df_mods, df_subs])
 .sort_values(['nome', 'meses_subs'])
 .drop_duplicates(subset = ['nome'])
 .fillna(0))