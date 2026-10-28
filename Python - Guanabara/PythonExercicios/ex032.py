from datetime import date
a = int(input('Digite um ano qualquer ou digite 0 para analisar o ano atual: '))
if a == 0:
    a = date.today().year # ---> Ou seja, ele vai pegar a data de hoje e só o ano.
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:     # Esse programa pega o ano
    print('{} é um ano bissexto.'.format(a))       #   configurado na máquina.
else:
    print('{} não é bissexto.'.format(a))

# Errei por falta de atenção. Era para usar o mesmo raciocínio do ex 30.

# "Nunca pare de estudar por mais difícil que as coisas possam parecer.
# Sempre tem uma saída se você for persistente. Persista! Sempre treine
# e nunca desista"
#        - Gustavo Guanabara.