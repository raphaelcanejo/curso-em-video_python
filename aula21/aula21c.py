def somar(a=0, b=0, c=0):
    s = a + b + c
    return s        # Vai fazer a chamada normalmente 1 pro a, 23 pro b, 11 pro c


resp = somar(1, 23, 11)

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
