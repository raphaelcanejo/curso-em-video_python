# >> Digitar help() no Python console.
# >> help(print)
# Parâmetros: i = inicio | f = fim | p = passo
# Como criar um DOCSTRING, manual que explica ocmo a função funciona.

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela:
    :param i: Início da contagem.
    :param f: Fim da contagem.
    :param p: Passo da contagem.
    :return: Sem retorno
    Criado por Raphael Canejo
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p   # c = c + p
    print('FIM!')

contador(1, 10, 1.5)
help(contador)
