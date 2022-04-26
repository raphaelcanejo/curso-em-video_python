# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []

for c in range(0, 5):
    num = int(input('Digite um número: '))

    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Valor adicionado a lista...')
    else:
        posicao = 0
        while posicao < len(valores):
            if num <= valores[posicao]:
                valores.insert(posicao, num)
                print(f'Valor adicionado na posição {posicao} da lista...')
                break
            posicao += 1

print('-=' * 25)
print(f'Os valores adicionados a lista, em ordem, foram {valores}')
