#  Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

print('-=' * 15)
s1 = float(input('PRIMEIRO SEGMENTO: '))
s2 = float(input('SEGUNDO SEGMENTO: '))
s3 = float(input('TERCEIRO SEGMENTO: '))
print('-=' * 15)
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
    print('Os segmentos acima PODEM formar um triângulo ', end='')
    if s1 == s2 == s3:
        print('EQUILÁTERO!')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')

