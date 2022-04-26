# Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS.
# No final, mostre quantas pessoas ainda não atingiram a maioridade a quantas já são maiores.

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print('Tivemos {} pessoas maiores de idade.'.format(totmaior))
print('Tivemos {} pessoas menores de idade'.format(totmenor))
