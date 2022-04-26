# Desenvolva um programa que leia o PRIMEIRO TERMO e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

# an == a1 + (n - 1) * r
print('-=' * 10)
n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: ')) # r significa a razão
decimo = n1 + (10 - 1) * r # O 10-1 é porque queremos achar o décimo termo, essa é uma fórmula mateática conhecida an == a1 + (n - 1) * r

for c in range(n1, decimo + r, r):
    print(c, end=' -> ')
print('FIM!')