def fatorial(num=1):
    f = 1       # Variável local
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))        # Variável global
print(f'A fatorial de {n} é igual a {fatorial(n)}.')

f1 = fatorial(7)
f2 = fatorial(6)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')
