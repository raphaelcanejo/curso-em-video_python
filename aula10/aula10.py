        # if -> se | else -> senão

''' 
nome = str(input('Qual é o seu nome? ')).strip()
 if nome == 'Raphael':
     print('Que nome lindo você tem.')
 else:
     print('Olá {}, que nome feio.'.format(nome))
 print('Boa noite, {}'.format(nome)) 
 '''

n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Parabéns! Sua média foi boa.')
else:
    print('Sua nota está abaixo da média, estude mais.')