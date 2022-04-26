# Crie um programa que faça o computador jogar Jokenpô com você.

print('-=' * 15)
from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA' ) # pedra é o item 0, papel item 1 e tesoura item 2.
computador =  randint(0, 2) # o computador vai randomizar entre pedra, papel e tesoura
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('-=' * 15)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ...')
sleep(1)
print('-=' * 15)
print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Você VENCEU!')
    elif jogador == 2:
        print('O computador VENCEU!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('O computador VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Você VENCEU!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('Você VENCEU!')
    elif jogador == 1:
        print('O computador VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')
        