v = float(input('Qual a velocidade do veículo, em km/h? '))
m = v - 80
m2 = m * 7
if v <= 80:
    print('Está-se dentro do limite de velocidade.')
else:
    print('Infringiu-se o limite de velocidade. Você foi multado!')
    print('Como a multa por cada km excedido é de R$7,00,\nvocê terá que pagar'
          ' R${:.2f}'.format(m2))

# Certinho