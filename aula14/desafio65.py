# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} valores e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))

# Como eu tentei fazer e não conseguir terminar
'''
num = 0
cont = 0
soma = 0
quant = int(input('Você deseja digitar quantos valores? '))
while cont != quant:
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    media = soma / cont
    if cont == quant:
        esc = str(input('Deseja continuar a digitar valores [S/N]? ')).strip().upper()
        if esc == 'S':
            quant = int(input('Você deseja digitar mais quantos valores? '))
            num = int(input('Digite um número: '))
            cont += 1
            soma += num
        elif esc == 'N':
            print('A soma dos valores digitados é {} e a média dos valores digitados é {}'.format(soma, media))
print('FIM!')
'''