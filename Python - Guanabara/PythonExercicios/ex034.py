from time import sleep
s = float(input('Qual o salário do funcionário? '))
print('Analisando aumento....')
sleep(3)
a10 = s * 0.1
a11 = s + a10
a15 = s * 0.15
a16 = s + a15
if s <= 1250:
    print('Você ganhou um aumento de 15%! Seu salário agora é de '
          'R${:.2f}'.format(a16))
else:
    print('Você ganhou um aumento de 10%! Seu novo salário é de '
          'R${:.2f}'.format(a11))

# Certinho.