# Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços.
# EXEMPLOS: apos a sopa | a sacada da casa | a torre da derrota | o lobo ama o bolo | anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip().upper() # Remove os espaços antes de depois da frase e joga tudo pra maiúsculo
palavras = frase.split() # Vai separar as palavras da frase onde tem os espaços, como uma lista ou vetor
junto = ''.join(palavras) # Vai juntar todas as palavras em apenas uma string, substituindo os pespaços por nada

'''
inverso = ''
'''

inverso = junto[::-1] # Vai peggar o junto do inicio ao fim de trás pra frente (-1), dessa forma não precisa usar a estrutura de repetição for

'''
for letra in range(len(junto) - 1, -1, -1): # Inverte a frase
    inverso += junto[letra]
'''

print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')
