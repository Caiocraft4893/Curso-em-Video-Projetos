'''
n = str(input('Digite seu nome todo: ')).strip().split()
print('Seu primeiro nome é {}'.format(n[0]))
print('E seu último nome é {}, certo?'.format())
'''

# Errei essa pelo mesmo motivo da 26: o 1.

# Maneira do Guanabara:

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

'''
Importante: como sabemos, o len, mostra o comprimento do que 
é atribuído a ela. Então quando fazemos len(nome), no exemplo
acima, saberemos qual as posições de nome.
Então eu posso fazer com que ele me mostre o nome (nome ,
na posição len de nome  [len(nome) , menos 1 -1])):
(nome[len(nome)-1])).
Menos 1 porque é para pegar o útimo nome (string) da lista

Ex:

nome = 'Pedro Souza Matos'
nome.split() = ['Pedro', 'Souza', 'Matos'] --> só tem 3 (de 0 até 2) 
(1 a menos, porque ele conta o 0). Por isso o 1 a menos.
 
Logo: print('Seu último nome é {}.format(nome[len(nome)-1]))
O programa exibiria: Matos.
'''