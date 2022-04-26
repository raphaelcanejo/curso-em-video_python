# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
from time import sleep
atual = date.today().year
print('-=' * 30)
print('QUAL O SEU SEXO:')
print('''[ 1 ] HOMEM
[ 2 ] MULHER''')
sexo = int(input('QUAL A SUA OPÇÃO? '))
print('-=' * 30)
if sexo == 2:
    print('No Brasil mulheres não precisam se alistar.')
elif sexo == 1:
    nasc = int(input('ANO DE NASCIMENTO: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    print('-=' * 30)
    print('PROCESSANDO...')
    sleep(2)
else:
    print('OPÇÃO INVÁLIDA! Tente novamente.')
if sexo == 1 and 18 == idade:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif sexo == 1 and idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = saldo + atual
    print('Seu alistamento será em {}.'.format(ano))
elif sexo == 1 and idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Você deveria ter se alistado em {}.'.format(ano))
