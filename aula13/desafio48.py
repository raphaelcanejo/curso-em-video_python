# Faça um programa que calcule a SOMA entre todos os NÚMEROS IMPARES que são MÚTIPLOS DE TRÊS
# e que se encontram no intervalo de 1 até 500.

soma = 0 # Isso é um acumulador
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de {} valores solicitados é {}'.format(cont, soma))
