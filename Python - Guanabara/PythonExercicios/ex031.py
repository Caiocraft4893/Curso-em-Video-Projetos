k = float(input('Qual a distância, em km? '))
p = 0.50 * k
p3 = 0.45 * k
if k <= 200:
    print('A distância da viagem foi {}, então dará R${:.2f}'.format(k, p))
else:
    print('A distância foi {}km, então você pagará R${:.2f} de '
          'passagem'.format(k, p3))

# Certinho

# Ou pode ser assiim tbm

# p = k * 0.50 if k <= 200 else k * 0.45  --> if simplificado