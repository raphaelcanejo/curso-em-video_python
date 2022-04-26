# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

val = []
val_par = []
val_impar = []

while True:
    val.append(int(input('Digite um número: ')))

    perg = str(input('Deseja continuar [S/N]? ')).upper()[0]

    if perg == 'N':
        print('Fim!')
        break

for i, v in enumerate(val):
    if v % 2 == 0:
        val_par.append(v)
    elif v % 2 == 1:
        val_impar.append(v)

print('-=' * 20)
print(f'A lista completa é {val}')
print(f'A lista de números pares é {val_par}')
print(f'A lista de números ímpares é {val_impar}')
