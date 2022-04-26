# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# ex: escreva('Olá, MMundo!') saída:
# ~~~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~~~

# Função
def escreva(txt):
    """Mensagem enfeitada

    Args:
        txt (String): Mensaguem que vai aparecer entre ~~
    """

    tam = len(txt) + 4

    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


# Programa Principal
escreva('Olá, Mundo!')
escreva('Raphael Canejo Dantas')
