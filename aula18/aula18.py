                # LISTAS dentro de LISTAS - LISTAS COMPOSTAS
#Listas ficam entre colchetes ou list()

teste = list()         # Lista teste
teste.append('Raphael')
teste.append(26)


galera = list()      # Lista galera
'''
galera.append(teste)    # Lista teste dendro da lista galera -> [galera[teste]]
                        # Quando eu faço isso estou criando uma ligação entre as listas, se forem alterados valores em teste
                        # em galera os mesmos valores serão alterados devido a ligação entre as listas.
                        # Para que isso não aconteça eu devo fazer uma cópia da lista [:]. 
'''

galera.append(teste[:])        # Aqui eu crio uma cópia da lista
teste[0] = 'Maria'             # Se fosse galera.append(teste) Vai mudar os valores tanto na lista teste quanto na lista galera
teste[1] = 22                  # se for galera.append(teste[:]) só muda os valores da lista teste, galera continua como a cópia de teste antes da mudança dos valores.

''' galera.append(teste) '''
galera.append(teste[:])

print(teste)
print(galera)

print('===' * 20)

gang = [['João', 20], ['Ana', 29], ['Akira', 17], ['Tetsuo', 15]]   # QUATRO listas dentro de uma lista grandona que englobam as 4.
                                                                    # Aqui cada lista dentro da grandona terá um índice que começa no zero, igual no fateamento de string
print(gang)

print('===' * 20)

print(gang[0]) # ['João', 20]
print(gang[1]) # ['Ana', 29]
print(gang[2]) # ['Akira', 17]
print(gang[3]) # ['Tetsuo', 15]

print('===' * 20)
                    # Os itens das listas que estão dentro da lista grandona também tem indices.
print(gang[0][0])
print(gang[1][0])   # o [1] É referente ao indice da lista completa, dentro da grandona, ['Ana', 29] e o [0] é referente apenas ao 'Ana' na lista menor.
print(gang[2][0])
print(gang[3][0])

print('===' * 20)

for p in gang:      # OUTRA forma de mostrar as listas pequenas completas que estão dentro da grandona
    print(p)

print('===' * 20)   # Se eu quiser que me mostre apenas os nomes

for p in gang:
    print(p[0])     # Vai mostrar só o nome.
    print(p[1])     # Vai mostrar só a idade.

print('===' * 20)   # Uma forma mais bonita de fazer o exemplo acime.

for p in gang:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('===' * 20)  # Também posso pedir para o usuário digitar os dados.

turma = list()
dados = list()     # Essa estrutura de dados, essa lista, será uma estrutura auxiliar para eu pegar/coletar os dados para depois enviar para uma estrutura principal que é a turma.
totmaior = totmenor = 0 # Esse tipo de simplificação só é possível em variáveis simples, em listas/ variáveis compostas não funciona.

for c in range(0, 4):    # Esse bloco é para eu ler os dados digitado pelo usuário e depois jogar para a lista turma
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    print('~~~' * 20)
    turma.append(dados[:])      # Estou criando uma cópia dos dados para a lista turma.
    dados.clear()               # Estou limpando os valores inseridos na lista dados.
                                # Se eu esquecer de fazer a cópia [:] no turma.append(dados[:]),
                                # quando eu der o comando dados.clear() o python vai apagar os valores de todas as listas,
                                # pois ai eu estaria criando uma ligação e não uma cópia da lista dados para turma.
print(turma)

for p in turma:         # Nesse bloco eu analiso para saber se as pessoas são maiores ou menores de idade
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos um total de {totmaior} maiores de idade e um total de {totmenor} menores de idade.')
