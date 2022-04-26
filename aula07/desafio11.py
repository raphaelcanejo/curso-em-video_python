# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade necessária para pinta-la, sabendo que
# Cada tipo de tinta, pinta uma área de 2m^2.

l = float(input('Digite a largura (m) da parede: '))
a = float(input('Digite a altura (m) da parete: '))
ar= l*a
t = ar/2
print('Sua parede tem a dimensão de {}X{}, que corresponde a uma área de {}m².'.format(a, l, ar))
print('Para pintar essa parede você precisará de {}l de tinta. '.format(t))
