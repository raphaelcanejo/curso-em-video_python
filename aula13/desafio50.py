# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma apenas daquelas que forem PARES.
# Se o valor digitado for ÍMPAR, desconsidere-o.

print('-=' * 8)
print('=====SOMADOR=====')
s = 0
for c in range(1, 7):
    n = int(input('Digite o {}° número: '.format(c)))
    if n % 2 == 0:
        s += n
print('A soma de todos os valores PARES é {}'.format(s))
