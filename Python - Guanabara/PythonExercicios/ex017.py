'''
from math import sqrt
co = float(input('Quanto mede o cateto oposto? '))
ca = float(input('Quanto mede o adjacente? '))
h = (ca ** 2) + (co ** 2)
hp = sqrt(h)
print('A hipotenusa vale {:.2f}'.format(hp))
'''

# ou....

from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = hypot(co, ca)
print('A hipotenusa vale {:.2f}'.format(h))

# certinho - os dois códigos