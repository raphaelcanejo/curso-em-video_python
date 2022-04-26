# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas (acima de 80Kg).
# C) Uma listagem com as pessoas mais leves (Abaixo de 80kg).

temp = []  # lista temporária
princ = []  # lista principal
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        maior = menor = temp[1]  # temp[1] é o peso das pessoas
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()

    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break

print('-=' * 30)

print(f'Ao todo, você cadastrou {len(princ)} pessoas.')

print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()

print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
