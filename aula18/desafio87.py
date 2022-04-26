# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# Variáveis
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
soma_par = maior = soma_coluna = 0

print('-=' * 25)
print('[linha, coluna]')
print('-=' * 25)

# Matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 25)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')

# A) A soma de todos os valores pares digitados.
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()

print('-=' * 25)

print(f'A soma dos valores pares é {soma_par}')

# B) A soma dos valores da terceira coluna.
for linha in range(0, 3):
    # Coluna [2] é a que quero somar, portanto, fica fixa, o que varia é a linha
    soma_coluna += matriz[linha][2]
print(f'A soma dos valores da coluna terceira é {soma_coluna}')

# C) O maior valor da segunda linha.
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')
