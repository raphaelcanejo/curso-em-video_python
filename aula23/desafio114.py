# Crie um código em Python que teste se o site pudim (http://pudim.com.br/) está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLerror:
    print('O site <http://pudim.com.br> não está acessível no momento.')
else:
    print('Consegui acessar o site <http://pudim.com.br> com sucesso!\n')
    # print(site.read()) Mostrar o código fonte do site, o conteúdo HTML
