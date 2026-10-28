'''n = int(input('Digite um número: '))
n1 = n + 1
n2 = n - 1
print('O sucessor desse número é {} e seu antecessor é {}'.format(n1, n2))
'''

n = int(input('\033[1;32mDigite um número: '))
print('\033[1;35mSeu antecessor é {} e seu sucessor {}'.format(n - 1, n + 1))


'''
Esse é um dos casos que escolhemos qual melhor jeito de usar 
o .format()
'''

# certinho