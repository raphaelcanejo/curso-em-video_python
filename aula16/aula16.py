# lanche = () [] {} >>> No Python podemos declarar uma variável composta dessas três formas:

# [] pode ser usado como list()

# Tuplas >>> Ficam entre PARÊNTESES >> A partir do Pytho 3.5 eu acho nem precisa por entre parênteses.
# Listas >>> Ficam entre COLCHETES
# Dicionários >>> Ficam entre CHAVES

# EM EXECUÇÃO NÃO POSSO ALTERAR VALORES DA TUPLA

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') # 0 -> Hambúrguer, 1 -> Suco, 2 -> Pizza, 3 -> Pudim == 4 VALORES
                                                  # -4 -> Hambúrguer, -3 -> Suco, -2 -> Pizza, -1 -> Pudim
print('=' * 30)

print(lanche)       # Mostra todos os itens da TUPLA
print(lanche[1])    # Quando é pra pedir um valor da variável em específico é sempre entre COLCHETES.
print(lanche[0:2])  # Reproduz o valor 0 e 1, o valor 2 é ignorado assim como no tratamento de strings.
print(lanche[:3])   # Mostra até o valor 2, ignora o valor 3
print(lanche[-2])
print(lanche[-2:])  # Começa na pizza e vai até o final
print(lanche[:-2])  # Mostra a partir da pizza, até o final;
print(len(lanche))  # Mostra quantos valores tem dentro da TUPLA

# lanche [1] = 'Refrigerante' >>> Se for executado esse código da erro, não tem como assimilar valores a TUPLA a não ser no momento que ela é declarada

print('=' * 30)

for comida in lanche:   # Vai repetir o looping até comer todos os lanches
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('=' * 30)     # Duas formas de fazer o mesmo algoritmo, tem momentos que apenas uma delas será executada

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba')

print('=' * 30)

for pos, alimento in enumerate(lanche):
    print(f'Eu vou comer {alimento} na posição {pos}')
print('Comi pra caramba')

# QUalquer uma das três soluções podem ser aplicadas, cada uma é melhor para casos diferentes.

print('=' * 30)

print(sorted(lanche))   # Coloca os lanches em ordem, e transforma em LISTA, quando executar eles vão estrar entra COLCHETES

print('=' * 30)

a = (1, 5, 3)
b = (4, 5, 6, 7)
c = a + b           # Cola uma TUPLA na outra, junta as duas
d = b + a           # A ordem que são coladas é diferente de c
print(c)            # Não é a mesma coisa que somar números, TUPLAS são estruturas compostas
print(len(c))
print(c.count(5))       # Quantas vezes o número 5 aparece em c
print(c.index(6))       # Em que posição está o número 6
print(c.index(5, 3))    # Em que posição está o 5 a partir da posição 3
print(d)
print(len(d))

print('=' * 30)

pessoa = ('Raphael', 26, 'M', 93.5) # Aceita números e letras, tanto faz, pode misturar
print(pessoa)
del(pessoa)     # Esse comando deleta a TUPLA. Não é possível alterar um valor da dupla mas pode deletar a tupla inteira
