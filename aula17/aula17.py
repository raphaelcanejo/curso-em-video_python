print('=' * 20)

num = [0, 1, 3, 2]
num[2] = 4          # Como dito, nas LISTAS é possível inserir valores no lugar de outros. LISTAS são mutáveis. O número no índice 2 será trocado pelo número 4.
num.append(7)       # Adiciona valores na LISTA. NEsse caso adicionei o valor 7, que aparece como o último elemento da LISTA.
num.sort()          # Organiza os valores, coloca eles em ordem.
''' num.sort(reverse=True)      #Vai colocar os valores em ordem inversa '''
num.insert(0, 2)    # Esse comando faz com que na posição/índice 0 vou colocar o número 2, dessa forma, os indices dos outros valores são alterados "jogados para frente" refazendo os índices
num.pop()           # Esse comando faz com que o último valor da lista seja ELIMINADO. No caso dessa lista o valor 7 será eliminado.
''' num.pop(2)      # Faz com que o valor que está na posição/índice 2 será eliminado '''
num.remove(2)       # Esse comando remove o valor 2 que estiver dentro da lista. É importante destacar que vai ELIMINAR apenas o PRIMEIRO valor 2 que encontrar na lista, indo na sequência dos indices.
                    # Se pedir para remover um valor que não está na lista vai da erro no código
'''
if 4 in num:        # O operador in do python é muito poderoso, pode ajudar em diversos cenários
    num.remove(4)
else:
    print('Não achei o número 4.')
'''

print(num)
print(f'Essa lista tem {len(num)} elementos.')      # len(num) me retorna quantos valores tem na lista.

print('=' * 20)

valores = list()         # Uma forma de inserir valores em uma lista, ou pedindo pro usuário adicionart
valores.append(5)
valores.append(9)
valores.append(4)

for valor in valores:
    print(f'{valor}...')

print('=' * 20)

for c, valor in enumerate(valores):              # c vai mostrar o indice a que o valor está inserido
    print(f'Na posição {c} encontrei {valor}!')
print('Cheguei ao final da lista')

print('=' * 20)

# O USUÁRIO inserindo valores na LISTA.

n = list()
for cont in range(0 , 5):
    n.append(int(input('Digite um valor: ')))
print(n)
for indice, v in enumerate(n):
    print(f'Na posição {indice} encontrei o valor {v}.')

print('=' * 20)

a = [2, 3, 4, 7]
b = a
b[2] = 8    # Vai inserir o valor 8 no indice 2. É importante notar que o valor 8 vai ser inserido tano na lista A quanto na lista B.
            # Quando acontece isso dizemos que o python está fazendo uma LIGAÇÃO de uma lista com a outra.
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('=' * 20)

# Quando eu quero criar uma CÓPIA de outra lista, fazemos o seguinte:

q = [6, 7, 8, 9]
w = q[:]           # [:] significa que vai fazer uma cópia da lista. w recebe todos os valores de q, não faz uma ligação faz uma cópia.
w[2] = 0           # Vai incerir o valor 0 no indice 2 na lista W apenas.
print(f'Lista Q: {q}.')
print(f'Lista W: {w}.')
