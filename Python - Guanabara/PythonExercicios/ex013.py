s = float(input('Quanto é o salário do funcionário? '))
a = (15 / 100) * s
ns = s + a
print('O funcionário agora ganhou um aumento de 15%,\n o que '
      'significa que seu novo salário é de R${:.2f}'.format(ns))

# certinho