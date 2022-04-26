# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

# como fiz da primeira vez
'''
from math import factorial
num = int(input('Digite um número para calcular seu FATORIAL: '))
fac = factorial(num)
print('O FATORIAL de {} é {}'.format(num, fac))
'''

num = int(input('Digite um número para calcular seu FATORIAL: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    if c > 1:                           # pode ser feito como: print(' x ' if c > 1 else ' = ', end='')
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='')