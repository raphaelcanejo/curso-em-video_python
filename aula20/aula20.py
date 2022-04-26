def titulo(txt):  # DEFINIÇÃO DE FUNÇÃO
    print('=' * 25)  # Eu tenho isso aqui como uma ROTINA, algo que acontece constantemente no meu programa
    print(txt)  # Coisas que acontecem constantemente o ideal é eu criar uma FUNÇÃO, exatamente como foi feito aqui.
    print('=' * 25)

    # As funções só teram realmente utilidade quando os códigos começarem a ficar grandes e repetitivos.


# Programa Principal 1
titulo('CURSO EM VÍDEO DE PYTHON')


# SEMPRE PULAR DUAS LINHAS ENTRE A def E O PROGRAMA PRINCIPAL

def soma(a, b):  # a e b dentro do parênteses são parametros
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal 2
soma(a=10, b=12)  # Se eu quiser explicitar os parâmetros, preciso fazer com os dois.
soma(b=5, a=8)  # Se eu quiser mudar a ordem dos parâmetros na hora de declarar.
soma(9, 6)

'''
a = 10
b = 12
s = a + b
print(s)

a = 5
b = 8
s = a + b
print(s)

a = 9
b = 6
s = a + b
print(s)
'''

print('=' * 25)


# Programa Principal 3
def contador(*num):  # Estou dizendo para o Python "Vou receber vários parâmetros, quantos? não sei"
    # print(num)          # Vai criar três tupla. Dessa forma, é possível fazer tudo que é possível fazer com uma tupla.
    for valor in num:       # Estou DESEMPACOTANDO pois dentro de num tem vários valores e no ecemplo que quero mostrar alguns, desempacontando.
        tam = len(num)                  # Em alguns momentos é melhor usar desempacotamento e em outros usar as listas, que é o que foi feito no próximo exemplo.
        print(f'{valor}', end=' ')
    print(f'Recebi {tam} números ao todo.')
    print('FIM!')


contador(2, 1, 7)
contador(0, 8)
contador(4, 4, 6, 2, 9)

print('=' * 25)
                            # Para o Python toda passagem de parâmetro é feita por refrência

# Programa Principal 4
# USANDO def COM LISTAS
def dobra(lista):
    posicao = 0
    while posicao < len(lista):  # Enquanto a posição for menor que o tamanho da lista multiplique a posição por dois
        lista[posicao] *= 2      # Tudo que eu fizer no parâmetro (lista) irá interferir na lista de valores. Nesse exemplo eu quero dobrar os números na lissta de valores.
        posicao += 1


valores = [2, 5, 7, 10]
dobra(valores)
print(valores)
