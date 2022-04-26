# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('-=' * 20)
preco = float(input('QUAL O VALOR DO PRODUTO? R$'))
print('-=' * 20)
print('''Formas de pagamento:
[ 1 ] Dinheiro/ Cheque à VISTA: 10% de desconto
[ 2 ] Cartão à VISTA: 5% de desconto
[ 3 ] 2x no cartão: Preço formal
[ 4 ] 3x ou mais no cartão: 20% de juros''')
op = int(input('Como deseja pagar? '))
print('-=' * 20)
if op == 1:
    dinche = preco - (preco * 0.10)
    print('Você pagará R${:.2f}'.format(dinche))
elif op == 2:
    cartao = preco - (preco * 0.05)
    print('Você pagará R${:.2f}'.format(cartao))
elif op == 3:
    x2 = preco / 2
    print('Você pagará duas prestações de R${:.2f}, totalizando R${:.2f}'.format(x2, preco))
elif op == 4:
    par = int(input('Deseja pagar em quantas vezes? '))
    pres = preco / par
    x3 = preco + (preco * 0.20)
    print('Você pagará {} parcelas de R${:.2f}, totalizando R${:.2f}'.format(par, pres, x3))
else:
    print('OPÇÃO INVÁLIDA! Tente novamente.')
print('-=' * 20)
print('BOAS COMPRAS! Volte sempre.')
