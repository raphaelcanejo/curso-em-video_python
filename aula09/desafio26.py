# Crie um programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes aparece a letra "A";
# -> Em que posição ela aprece a primeira vez;
# -> Em que posição ela aparece a última vez.

print('Analisador de frases')
frase = str(input('Digite alguma frase: ')).strip().upper()
print('A letra |a| aparece {} vezes'.format(frase.count('A')))
print('A letra |a| aparece pela primeira vez na posição {}'.format(frase.find('A') + 1))
print('A letra |a| aparece pela última vez na posição {}'.format(frase.rfind('A') + 1))
