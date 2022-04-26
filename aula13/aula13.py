        # for -> laço | in -> no | range -> intervalo

for c in range(0, 6): # Nesse caso ele vai repetir 'Oi' 6 vezes, se eu colocar o range (1, 6) ele vai repetir o 'Oi' 5 vezes.
    print('Oi')
print('FIM!')
print('-=' * 20)

for c in range(1, 7): # Nesse caso ele conta de 1 até 6.
    print(c)
print('FIM!')
print('-=' * 20)

for c in range(6, 0, -1): # Como eu quero que ele conte de 6 até 0 tenho que adicionar o -1
    print(c)              # que vai dizer para o programa qual a interação.
print('FIM!')
print('-=' * 20)

for c in range(0, 7, 2): # Essa interação com o 2 vai dizer para o programa fazer a contagem de 2 em 2
    print(c)
print('FIM!')
print('-=' * 20)

n = int(input('Digite um número: '))
for c in range(0, n + 1): # Esse n + 1 faz com que a contagem final de fato chegue até o número que o usuário digitar
    print(c)
print('FIM!')
print('-=' * 20)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(1, f+1, p):
    print(c)
print('FIM!')
print('-=' * 20)

for c in range(0, 4):
    n = int(input('Digite um número: '))
print('FIM!')
print('-=' * 20)

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor:'))
    s += n  # Isso é equivalente a '''s = s + n'''
print('A soma de todos os valores foi {}'.format(s))
print('-=' * 20)
