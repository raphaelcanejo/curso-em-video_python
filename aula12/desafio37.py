# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO.
# 1 para binário
# 2 para octal
# 3 para hexadecimal

print('-=' * 25)
num = int(input('Digite um número INTEIRO: '))
print ('''Escolha uma das BASES para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
print('-=' * 25)
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num) [2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num) [2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num) [2:]))
else:
    print('OPÇÃO INVÁLIDA! Tente novamente.')

# O [2:] é o tratamento de string para remover os dois primeiros caracteres de cada conversão que são irrelevantes para o resultado final.