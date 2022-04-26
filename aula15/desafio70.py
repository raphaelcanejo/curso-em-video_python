# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

tot = tot_mil = menor = cont = 0
barato = ''     # O espaço começa sem nada porque não temos produto cadastrado ainda
while True:
    produto = str(input('NOME DO PRODUTO: ')).strip().lower()
    preco = float(input('PREÇO DO PRODUTO: R$'))
    cont += 1
    tot += preco
    if preco > 1000:
        tot_mil += 1
    if cont == 1 or preco < menor:       # Se for o primeiro produto # Se não for o primeiro produto
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        print('-=' * 20)
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${tot:.2f}')
print(f'Temos {tot_mil:.2f} produtos custando acima de R$1000')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')