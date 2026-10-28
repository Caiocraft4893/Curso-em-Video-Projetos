'''
from math import sin, cos, tan
a = float(input('Quanto mede o ângulo? '))
s = sin(a)
c = cos(a)
t = tan(a)
print('O seno deste ângulo é {:.2f}, o cosseno {:.2f} e'
      ' a tangente {:.2f}'.format(s, c, t))
'''

# fiz errado.


# parece que eu vou ter converter as medidas do ângulos para
# radianos.

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
'''         ^
            ^---> Ali eu estou fazendo o seguinte: vou pegar
o ângulo que eu digitei, converto para radianos, vou pegar
esse ângulo já convertido pra radianos e calcular seu seno.
'''
print('O ângulo de {} tem o seno de {:.2f}'.format(an, seno))
cos = cos(radians(an))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tan))

# Precisei da correção. Não tive essa matéria na escola.
