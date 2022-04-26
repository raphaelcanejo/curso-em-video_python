# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
pc = randint(0, 11)
contador = 0

while True:
    player_esc = str(input('você quer PAR ou ÍMPAR ? [P/I] ')).upper().strip()[0]
    player_num = int(input('Escolha um valor de 0 à 10: '))
    print(f'O computador jogou {pc}.')
    print('~' * 50)

    soma = player_num + pc

    if soma % 2 == 0:
        print(f'A soma de {player_num} e {pc} é {soma}, que é um valor PAR.')
        if player_esc == 'P':
            print('PARABÉNS! Você venceu.')
            print('~' * 50)
            contador += 1
        elif player_esc == 'I':
            print('VOCÊ PERDEU!')
            break
    else:
        print(f'A soma de {player_num} e {pc} é {soma}, que é um valor ÍMPAR.')
        if player_esc == 'P':
            print('VOCÊ PERDEU!')
            break
        elif player_esc == 'I':
            print('PARABÉNS! Você venceu.')
            contador += 1
            print('~' * 50)

print('~' * 50)
print(f'Você venceu {contador} partidas consecutivas.')