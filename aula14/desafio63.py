# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
# N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-=' * 12)
print('SEQUÊNCIA DE FIBONACCI')
print('-=' * 12)
n = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
print('-=' * 12)
print('{} -> {}'.format(n1, n2), end='')
cont = 3
while cont <= n:
    n3 = n1 + n2
    print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1
print(' -> FIM!')
