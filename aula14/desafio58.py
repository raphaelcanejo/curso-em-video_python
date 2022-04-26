# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)

print('Sou seu computador... \nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS... Tente mais uma vez.')
        elif jogador > computador:
            print('MENOS... Tente mais uma vez.')
print('PARABÉNS! Você acertou com {} tentativas.'.format(palpites))

# Como eu fiz
'''
from random import randint
computador = randint(0, 10)

print('Olá, sou seu computador... \nAcabei de pensar em um número entre 0 e 10.')
jogador = int(input('Será que você consegue adivinhar qual foi? '))
print('-=' * 20)
contador = 0
while jogador != computador:
    jogador = int(input('ERRROUU! Tente novamente. \nEm que número eu pensei? '))
    print('-=' * 20)
    contador += 1
if jogador == computador:
        print('PARABÉNS! Você acertou.')
        print('Você tentou {} vezes até acertar'.format(contador))
'''

# Desafio 28
'''
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
'''