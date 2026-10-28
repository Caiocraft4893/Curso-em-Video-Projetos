l = float(input('Quanto mede a largura? '))
a = float(input('Quanto é a altura? '))
ar = l * a
t = ar / 2
print('Sua parede tem {} X {} de dimensão e serão necessários\n {:.2f} litros'
      ' de tinta para pintar essa parede de {}m²'.format(l, a, t, ar))

# certinho