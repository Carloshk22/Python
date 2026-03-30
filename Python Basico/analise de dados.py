import pandas as pd

dados = {
    'nome': ['Produto A', 'Produto B', 'Produto B', 'Produto C'],
    'quantidade de itens comprados': [3, 5, 5, 8],
    'tipo de iten': ['Telefone', 'Computador', 'Computador', 'Ventilador'],
    'receita total': [1000, 300, 300, 45],

}

df = pd.DataFrame(dados)
print(df)

df.drop_duplicates(keep='last', inplace=True)
print(df)

df['preço do item'] = df['receita total']/df['quantidade de itens comprados']
itens_acima_50 = df[df['preço do item'] > 50]
print('Itens acima de 50 reais: ')
print(itens_acima_50)
