# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

print('=========ATENÇÃO==========')
print('PROMOÇÃO DE 5% DE DESCONTO')
p = float(input('Digite o preço do produto para aplicarmos o desconto: R$'))
d = p - (p*5)/100
print('O novo preço do produto é R${:.2f}'.format(d))
print('Obrigado pela preferência!')

