# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# considere a cotação US$1.00 = R$5.68

print('CONVERSOR DE MOEDA R$ -> US$')
real = float(input('Quantos Reais você tem? R$ '))
dolar = real * 5.68
print('Você pode comprar US$ {}.'.format(dolar))

