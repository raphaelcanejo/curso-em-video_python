# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep

# >>>>> Funções <<<<<


def linha(txt):
    """Mostra linhas com 20 espaços na tela

    Args:
        txt (str): Colocar o que eu quero que faça de linha
    """
    print(txt * 20)


def contador(i, f, p):
    """Contagem até onde eu quero contar

    Args:
        i (int): Onde a contagem começa.
        f (int): Onde a contagem termina.
        p (int): Passo, de quanto em quanto quero contar.
    """
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('~~' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# >>>>> Programa Principal <<<<<
contador(1, 10, 1)
contador(10, 0, 2)

linha('-=')
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio:    '))
fim = int(input('Fim:       '))
passo = int(input('Passo:   '))
contador(ini, fim, passo)
