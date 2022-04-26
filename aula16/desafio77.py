# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('amor', 'frajola', 'nina', 'ovo',
            'frio', 'notebook', 'chocolate',
            'pantanal', 'novela', 'onça')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aáàãâeéèêiíìîoóòõôuúùû':
            print(letra.upper(), end=' ')
