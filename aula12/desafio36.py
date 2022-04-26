# Escreva um programa para aprovar  um empréstimo bancário para a compra de uma casa.
# O programa vai perguntar O VALOR DA CASA, o SALÁRIO do comprador e EM QUANTOS ANOS ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
# Sem adição de juros.

print('-=' * 25)
vcas = float(input('QUAL O VALOR DA CASA: R$'))
sal = float(input('QUAL O SEU SALÁRIO: R$'))
ano = int(input('EM QUANTOS ANOS DESEJA PAGAR: '))
par = ano * 12
pres = vcas / par
sal30 = sal * 0.30
print('-=' * 25)
if pres > sal30:
    print('EMPRÉSTIMO NEGADO! \nO valor das prestações são maiores que 30% do seu salário.')
    print('{} PRESTAÇÕES DE: R${:.2f} \n30% DO SALÁRIO: R${:.2f} \n'.format(par, pres, sal30))
    print('Ou você arruma um salário maior ou pague a casa com mais prestações. \nTenha um bom dia!')
elif pres <= sal30:
    print('EMPRÉSTIMO APROVADO! \nA casa foi dividida em {} parcelas de R${:.2f}. \nTenha um bom dia.'.format(par, pres))
print('-=' * 25)

