# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

tot18 = tot_homens = tot_mulheres20 = 0

while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tot_homens += 1
    if sexo == 'F' and idade < 20:
        tot_mulheres20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {tot_homens} cadastrados.')
print(f'Ao todo temos {tot_mulheres20} mulheres com menos de 20 anos cadastradas.')

'''
print('CADASTRO DE PESSOAS')
pess = 0
mulheres = 0
homens = 0

while True:
    print('-=' * 15)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-=' * 15)
    op = str(input('DESAJA CONTINUAR? [S/N]')).strip().upper()[0]
    pess += 1
    while sexo not in 'MF':
        op = str(input('DESAJA CONTINUAR? [S/N]')).strip().upper()[0]
        if sexo == 'M':
            homens += 1
        elif sexo == 'F':
            mulheres += 1
        else:
            sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]


print(f'Foram cadastradas {pess} pessoas.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastradas {mulheres} mulheres.')
'''