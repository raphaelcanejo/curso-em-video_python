# Refaça o DESAFIO 09, mostrando a TABUADA de um número que o usuário escolher, só que agora utilizando um laço for.

print('=======TABUADA=======')
n = int(input('Digite um número para ver a tabuada: '))
print('-=' * 10)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))
print('-=' * 10)
