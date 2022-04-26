# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# COMO EU FIZ PELA PRIMEIRA VEZ
'''from random import choice
print('Jogo da Adivinhação')
print('Vou pensar em um número de 0 à 5, tente adivinhar qual é.')
n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = [n0, n1, n2, n3, n4, n5]
num = choice(lista)
n = int(input('Digite um número: '))
if n == num:
    print('Parabéns, você acertou o número.')
else:
    print('EROUUUU, tente novamente.')'''

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar me um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar o número que o computador pensou
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('EROOOUUU! Eu pensei no número {} e não no número {}.'.format(computador, jogador))
