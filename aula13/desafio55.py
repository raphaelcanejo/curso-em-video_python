# Faça um programa que leia o PESO de CINCO PESSOAS.
# No final, mostre qual foi o MAIOR e o MENOR peso lidos.

print('-=' * 15)
peso = 0
mais_pesado = 0
menos_pesado = 0

for c in range (1, 6):
    peso = float(input('DIGITE O SEU PESOda {}° PESSOA: '.format(c)))

    if c == 1:
        mais_pesado = peso
        menos_pesado = peso
    else:
        if peso > mais_pesado:
            mais_pesado = peso

        if peso < menos_pesado:
            menos_pesado = peso

print('A pessoa mais pesada tem {:.2f}Kg'.format(mais_pesado))
print('A pessoa menos pesada tem {:.2f}Kg'.format(menos_pesado))