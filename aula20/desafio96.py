# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

# Função
def area(largura, comprimento):
    """Calcular a área de um terreno
    Args:
        largura (float): Largura do terreno
        comprimento (float): Comprimento do terreno
    """
    a = largura * comprimento
    print(f'A área de um terreno {largura} X {comprimento} é de {a}m²')


# Programa Principal
print('     Controle de Terrenos        ')
print('--' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
