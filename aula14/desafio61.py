# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

print('Gerador de P.A')
print('-=' * 13)
p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = p1       # aqui ele me mostra o termo
contador = 1     # Aqui vai contar quantos termos foram

while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    contador += 1
print('FIM!')
