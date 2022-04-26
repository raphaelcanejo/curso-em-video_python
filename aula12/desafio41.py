# A Confederação Nacional de Natação precisa de um programa que leia o
# ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
ano = int(input('EM QUE ANO VOCÊ NASCEU: '))
idade = atual - ano
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Você está classificado na categoria MIRIM.')
elif idade <= 14:
    print('Você está classificado na categoria INFANTIL.')
elif idade <= 19:
    print('Você está classificado na categoria JÚNIOR.')
elif idade <= 25:
    print('Você está classificado na categoria SÊNIOR.')
else:
    print('Você está classificado na categoria MASTER.')

