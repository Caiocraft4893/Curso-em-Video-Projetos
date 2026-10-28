import random
from time import sleep
print('computador: vou pensar num número inteiro de 0 a 5 e você tem que '
     'adivinhar qual é, está bem?')
print('você: blz')

lista = 0, 1, 2, 3, 4, 5
e = random.choice(lista)
c = print('computador: Digite o número que você acha que eu escolhi '
          '(inteiro de 0 a 5):')
u = int(input('você: '))
print('Confirmando.....')
sleep(3)
if e == u:
    print('Parabéns, você acertou. Como você sabia?')
else:
    print('hmmm, Você errou.')
print('O número que eu escolhi foi: {}'.format(e))

# Certinho!
