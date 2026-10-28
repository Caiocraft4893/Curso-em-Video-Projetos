'''
from math import floor
n = float(input('Digite um número real: '))
i = floor(n)
print('A parte inteira deste número real é {}'.format(i))
'''

# meu jeito - usei o floor para arredondar para baixo,
# pelo visto não funciona, se usar número negativo.


from math import trunc
n = float(input('Digite um número real: '))
print('A parte inteira desse número é {}'.format(trunc(n)))


# jeito do guanabara importando a função truncate
# vou ter que usar um desses dois programas, pq
# o meu está errado

'''
n = float(input('Digite um número real: '))
print('A porção inteira desse número é {}'.format(int(n)))
'''


# outro jeito do guanabara, só que usando a função int
# sem importar nada

# nem sempre é necessário importar módulos:
# você pode fazer com o que a gente tem em casa!


# precisei da correção e de um comentário -> @M-xe2le - valeu
# por me mostrar meu erro.