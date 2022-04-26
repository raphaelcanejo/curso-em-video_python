# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'RB Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(f'Os 5 primeiros colocados são {times[:5]}')
print('-=' * 30)
print(f'Os times na zona de rebaixamento são {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O Fluminense está na {times.index("Fluminense")+1}ª posição')
