'''
r = float(input('Quanto mede a primeira reta? '))
r2 = float(input('Quanto mede o comprimento da segunda reta? '))
r3 = float(input('Quanto mede a terceira reta? '))
if (r2 - r3) < r < r2 + r3:
    print('É possível formar um triângulo com essas medidas!')
#if (r - r3) < r2 < r + r3:
    print('É possível formar um triângulo com essas medidas!')
#if (r - r2) < r3 < r + r2:
#    print('É possível formar um triângulo com essas medidas!')
else:
    print('Não é possível formar um triângulo com essas medidas!')
'''
# Meu jeito.
# A soma das medidas dos 2 lados tem que ser > o 3 lado, SEMPRE!

# Errei. Errei bonito.

# Jeito do Guanabara.

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triângulos')
else:
    print('Os segmenos acima não podem formar triângulos')
