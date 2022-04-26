# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = []

while True:
    valores.append(int(input('Digite um número: ')))

    perg = str(input('Deseja inserir mais valores [S/N]? ')).upper()[0]

    if perg == 'N':
        break


print('-=' * 20)

print(f'Foram digitados {len(valores)} números na lista.')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente {valores}')

if 5 in valores:
    print('O número 5 está inserido na lista.')
else:
    print('O número 5 não foi encontrado na lista.')
