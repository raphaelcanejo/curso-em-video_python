# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular/tabela.

materiais = (
    'Lápis', 1.75,
    'Borracha', 0.50,
    'Caneta', 2.25,
    'Caderno', 14.90,
    'Régua', 4.50,
    'Estojo', 8.90
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)

for posicao in range(0, len(materiais)):
    if posicao % 2 == 0:
        print(f'{materiais[posicao]:.<30}', end='')
    else:
        print(f'R${materiais[posicao]:>7.2f}')

print('-' * 40)
