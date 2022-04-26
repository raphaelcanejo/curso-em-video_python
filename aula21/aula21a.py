# Quando faço isso: a=0, b=0, c=0. Estou criando Parâmetros Opcionais.
# Parâmetros Opcionais significa que se o parâmetro não receber um valor, nesse caso, o parâmetro será igual a ZERO.

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Raphael Canejo
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 3, 3)
somar(2, 4)
somar()

help(somar)
