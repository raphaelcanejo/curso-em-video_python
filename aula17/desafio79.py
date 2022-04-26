# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []

while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado. Não vou adicionar!')

    r = str(input('Gostaria de continuar [S/N]? ')).upper()[0]
    if r in 'N':
        break
valores.sort()
print(f'Você adicionou os valores {valores}')
