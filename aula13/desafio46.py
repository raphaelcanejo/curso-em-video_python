# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício, indo de 10 ATÉ 0,
# com uma pausa de 1 SEGUNDO entre eles.

from time import sleep
print('Contagem regressiva para o estouro dos fogos de artifício')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
sleep(0.5)
print('BOOOM PÁ PÁ PÁ BOOOM PÁ!!!')
