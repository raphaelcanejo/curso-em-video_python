# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de P.A')
print('-=' * 25)
p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = p1       # aqui ele me mostra o termo
contador = 1     # Aqui vai contar quantos termos foram
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('-=' * 25)
print('P.A finalizada com {} termos mostrados'.format(total))
print('FIM!')