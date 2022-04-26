brasil = []     # Um lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}  # dicionário
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}       # dicionário
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)

print('===' * 20)

print(brasil)   # Vai mostrar na tela uma lista com dois elementos.
print(brasil[0])
print(brasil[1])

print('===' * 20)

print(brasil[0]['uf'])  # [0] representa o dicionário Rio de Janeiro na Lista.
print(brasil[0]['sigla'])
print(brasil[1]['uf'])  # [1] representa o dicionário São Paulo na lista.
print(brasil[0]['sigla'])

print('===' * 20)

