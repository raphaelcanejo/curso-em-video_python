print('\033[1;30;45mOlá, mundo!\033[m') # letra normal | letra branca | fundo lilás

nome = 'Raphael'
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format('\033[1;31;45m', nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'033[33m',
         'pb':'\033[7;30m'}   # Isso se chama dicionários, vamos estudar mais p/ frente
print('Olá, muito prazer em te conhecer, {}{}{}'.format(cores['pb'], nome, cores['limpa']))

'''
style                           text                back/fundo/cor de destaque
0 = none                        30 = branco         40 = branco
1 = bold/negrito                31 = vermelho       41 = vermelho
4 = underline/sublinhado        32 = verde          42 = verde
7 = negativo                    33 = amarelo        43 = amarelo
                                34 = azul           44 = azul
                                35 = lilás          45 = lilás
                                36 = ciano          46 = ciano
                                37 = cinza          47 =cinza
'''
