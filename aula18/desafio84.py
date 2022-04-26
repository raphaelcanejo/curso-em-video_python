# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas (acima de 80Kg).
# C) Uma listagem com as pessoas mais leves (Abaixo de 80kg).

# Variáveis
cadastro = []
dados = []
pesadas = []
leves = []
tot_pessoas = 0

# Programa
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))

    dados.append(cadastro[:])
    tot_pessoas += 1

    if cadastro[1] >= 80:
        pesadas.append(cadastro[0])
    elif cadastro[1] < 80:
        leves.append(cadastro[0])

    cadastro.clear()

    perg = str(input('Deseja adicionar mais alguém? [S/N] ')).upper()[0]
    if perg == 'N':
        print('Fim!')
        break

print('~~' * 20)

print(f'Foram cadastradas {tot_pessoas} pessoas.')
print(f'Pessoas pesadas {pesadas}')
print(f'Pessoas leves {leves}')
