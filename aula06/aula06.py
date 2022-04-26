n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1+n2
print('A soma vale', s)

print('-=' * 20)

n = input('Digite algo: ')

# o comando .is funciona como um método de teste de tipos. Como estou usando input direto o tipo será lido sempre como string.

print(n.isnumeric()) # vai me dizer se o que digitei é um número ou não.
print(n.isalpha()) # vai me dizer se o que digitei é letra ou não.
print(n.isalnum()) # vai me dizer se o que digitei é alfanumérico ou não.
print(n.isupper()) # vai me dizer se o que digitei está somente em letras maiúsculas.