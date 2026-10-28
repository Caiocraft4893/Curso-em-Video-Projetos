n = (float(input('Digite um número: ')))
u = n % 10  # --> unidade
d = n - u    # --> subtração do n com a unidade
d2 = d / 10   # --> n já subtraído, dividido p/ 10
d3 = d2 % 10  # --> dezena
c = d2 - d3  # --> n subtraído, dividido por 10, menos a dezena
c2 = c / 10  # --> n subtraído, dividido p/ 10, menos a dezena, dividido
c3 = c2 % 10  # --> centena                                       p/ 10
m = c2 - c3  # --> n subtraído, dividido p/ 10, menos a dezena, dvidido
m2 = m / 10  # --> milhar                        p/ 10, menos a centena
print('Esse número tem: ')
print(' {} unidades,\n {} dezenas,\n {} centenas\n e {} '
       'milhar'.format(u, d3, c3, m2))

# finalmente consegui!!!! Complicado abeça!

# valeu tutorial da intenet:
'''https://www.pythonprogressivo.net/2018/02/
Achar-Unidade-Dezena-Centena-de-um-Numero.html'''

# certinho.
# A prova de que também é possível fatiar um número
# usando a matamática.