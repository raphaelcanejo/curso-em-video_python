# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

print('~~~~~~~~~~~~TABUADA~~~~~~~~~~~~')
cont = n =  0
while True:
    n = int(input('Digite o número que quer saber a tabuada: '))
    if n < 0:
        break
    else:
        for cont in range(1, 11):
            mult = n * cont
            print(f'{n} x {cont} = {mult}')     # print(f'{n} x {cont} = {n * cont}')
print('FIM!')
