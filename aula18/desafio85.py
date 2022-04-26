# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

temp = []
impar = []
par = []
master = []

print('~~' * 20)

for c in range(0, 7):
    temp.append(int(input('Digite um número: ')))

    if temp[c] % 2 == 0:
        par.append(temp[c])
    elif temp[c] % 2 == 1:
        impar.append(temp[c])

par.sort()
impar.sort()

master.append(par)
master.append(impar)

print('~~' * 20)

print(f'Os valores pares foram {par}')
print(f'Os valores ímpares foram {impar}')
print(master)
