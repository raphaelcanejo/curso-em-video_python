# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
# O PRIMEIRO VALOR é MAIOR.
# O SEGUNDO VALOR é MAIOR.
# NÃO EXISTE valor maior, os dois são IGUAIS.

print('-=' * 15)
n1 = float(input('PRIMEIRO VALOR: '))
n2 = float(input('SEGUNDO VALOR: '))
print('-=' * 15)
if n1 > n2:
    print('O PRIMEIRO valor é MAIOR.')
elif n1 < n2:
    print('O SEGUNDO valor é MAIOR.')
else:
    print('Os valores são IGUAIS.')
