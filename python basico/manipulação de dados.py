import pandas as pd
from datetime import datetime as dt


df_selic = pd.read_json(
    'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2023')
(df_selic.info())
(df_selic)

df_selic.drop_duplicates(keep='last', inplace=True)

data_extração = dt.today()
df_selic['data_extração'] = data_extração
df_selic['responsavel'] = 'Carlin'
(df_selic.info())
(df_selic.head())

print(df_selic.loc[[1, 23, 248]])