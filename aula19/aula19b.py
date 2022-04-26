estado = {}  # Dicionário
brasil = []  # Lista

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip()
    estado['sigla'] = str(input('Sigla do estado: ')).strip().upper()
    print('===' * 20)
    # Nas listas para fazer uma cópia/fatiamento dos itens era necessário usar [:],
    brasil.append(estado.copy())
    # agora nos dicionários nós usamos o método "variável.copy()" para criar uma cópia.

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
