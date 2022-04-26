# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

import enum
from ssl import enum_certificates


jogador = {}
partidas = []
time = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()

    for c in range(0, tot):
        partidas.append(int(input(f'    - Quantos gols na partida {c+1}? ')))

    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'N':
        break

print('--' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('--' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 30)

while True:
    busca = int(input('Mostrar dados que qual jogado? [999 encerra] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} ---')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('--' * 30)

print('<<<<< PROGRAMA ENCERRADO >>>>>')
