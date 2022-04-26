#  Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for i in range(1, 6):
    valores.append(int(input(f'Digite um número para a {i}ª posição: ')))

print(f'Você digitou os valores {valores}')
print(f'O menor valor digitado foi {min(valores)}')
print(f'O maior valor digitado foi {max(valores)}')
