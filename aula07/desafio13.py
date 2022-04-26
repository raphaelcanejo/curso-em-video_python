# Faça um programa que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

print('CALCULE SEU SALÁRIO COM O NOVO AUMENTO DE 15%')
sal = float(input('Digite o valor do seu salário: R$'))
nsal = sal + (sal*15)/100
print('Se novo salário será de R${}.'.format(nsal))
