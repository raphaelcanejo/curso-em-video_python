# Faça um programa que leia um NÚMERO INTEIRO e diga se ele é ou não um NÚMERO PRIMO.

num = int(input('Digite um número: '))
tot = 0 # Para saber quantos números divisiveis tem
for c in range(1, num+1):
    if num % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Portanto, o número {} é PRIMO!'.format(num))
else:
    print('Portanto, o número {} NÃO É PRIMO!'.format(num))
