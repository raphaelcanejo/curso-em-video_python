# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

s = cont = 0
while True:     # True faz com que aconteça um looping infinito que só vai parar com o comando Break
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    s += n      # s -= 999 é uma gambiarra que pode ser usada para o 999 não entrar no valor final da soma
    cont += 1   # Só vai receber o cont + 1 se o n não for 999, assim o flag 999 não entra na contagem.
print(f'Você digitou {cont} valores e a soma entre eles é {s}.')
