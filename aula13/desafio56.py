# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS.
# No final do programa, mostre:
# A MÉDIA DE IDADE do grupo;
# Qual é o nome do homem MAIS VELHO;
# Quantas mulheres têm MENOS de 20 anos.

print('ANALISADOR DE PESSOAS')
print('-=' * 15)

idade = 0
soma = 0
cont_mulheres = 0
media = 0
maior = 0
homem_velho = 0

for c in range(1, 5):
    nome = str(input('DIGITE NOME DA {}° PESSOA: '.format(c))).strip().upper()
    idade = int(input('DIGITE SUA IDADE: '))
    sexo = str(input('DIGITE SEU SEXO [M/F]: ')).strip().upper()
    print('-=' * 15)

    soma += idade # Faz a soma entre todas as idades
    media = soma / 4 # Pega a soma das idade e divide pelo número de pessoas

    if sexo == 'M' and idade > maior:
        maior = idade
        homem_velho = nome

    if sexo == 'F' and idade < 20:
        cont_mulheres += 1

print('A média de idade do grupo é {:.2f} anos'.format(media))
print('O homem MAIS VELHO cadastrado é o {} e tem {} anos'.format(homem_velho, idade))

if cont_mulheres == 0:
    print('Não foi cadastradas mulheres no grupo.')
else:
    print('Ao todo temos {} mulheres com MENOS de 20 anos cadastradas'.format(cont_mulheres))
