# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quadro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

# while True:
#     num = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= num <= 20:
#         break
#     print('Tente novamente.')
# print(f'Você digitou o número {cont[num]}')

# Modificar esse programa para que ele só pare de perguntar que número o usuário quer
# quando o usuário disser que não quer

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))

        if 0 <= num <= 20:
            break
        else:
            print('Tente novamente.', end=' ')

    print(f'Você digitou o número {cont[num]}.')

    while True:
        dnv = input('Você quer tentar novamente? [S/N] ').lower().strip()
        if dnv == 's' or dnv == 'n':
            break
    if dnv == 'n':
        break
