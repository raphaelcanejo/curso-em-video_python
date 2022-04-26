# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = float(input('Digite o PRIMEIRO valor: '))
n2 = float(input('Digite o SEGUNDO valor: '))
op = 0

while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input('->>>>> Qual é a sua opção? '))
    print('-=' * 15)
    if op == 1:
        soma = n1 + n2
        print('RESULTADO: {:.0f} + {:.0f} = {:.0f}'.format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print('RESULTADO: {:.0f} X {:.0f} = {:.0f}'.format(n1, n2, mult))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif op == 4:
        print('Informe os números novamente:')
        n1 = float(input('Digite o PRIMEIRO valor: '))
        n2 = float(input('Digite o SEGUNDO valor: '))
    elif op == 5:
        print('FINALIZANDO...')
        sleep(2.5)
    else:
        print('OPÇÃO INVÁLIDA! Tente novamente.')
    print('-=' * 15)
print('FIM DO PROGRAMA!')
