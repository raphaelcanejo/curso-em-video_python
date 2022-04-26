nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

# print('Prazer em te conhecer {:20}!'.format(nome)) = Mostra o nome com 20 caracteres.
# print('Prazer em te conhecer {:>20}!'.format(nome)) = Mostra o nome com 20 caracteres e alinhado a direita.
# print('Prazer em te conhecer {:^20}!'.format(nome)) = Mostra o nome com 20 caracteres e centralizado.
# print('Prazer em te conhecer {:=^20}!'.format(nome)) = Mostra o nome com 20 caracteres, centralizado e com sinais de igual em volta do nome preenchendo os 20 caracteres.


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A soma entre os valores é {}.'.format(n1+n2))

# Tem como fazer operações aritméticas sem precisar adicionar mais uma variável com o resultado da operação.
# Só adicionamos mais uma variável para o resultado da operação se quisermos utilizar esse valor de novo no código, ai ele precisa ficar armazenado na memória.


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
d = n1 / n2
m = n1 * n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, a divisão {:.3}, o produto {}, a divisão inteira {} e a exponenciação {}'.format(s, d, m, di, e))

# {:.3} vai mostrar o resultado com três casas decimais.
# end=' ' vai juntar dois print na mesma linha. Se colocar algo dentro das aspas vai aparecer entre onde as linhas se juntaram
# /n vai quebrar a linha no meio do print.