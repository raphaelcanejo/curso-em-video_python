# Exercício 68 só que o código feito pelo professor Guanabara

from random import randint
v = 0

while True:
    jogador = int(input('Diga um valor '))
    pc = randint(0, 11)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
    print(f'você jogou {jogador} e o computador {pc}. Total de {total}.', end='')
    print('DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!!! Você venceu {v} vezes.')
