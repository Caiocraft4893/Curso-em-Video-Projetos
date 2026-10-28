'''
n = int(input('Digite um número: '))
print('Aqui está a tabuada deste número: ')
print('{} vezes 1 = {}'.format(n, n * 1), end='   ')
print('{} vezes 2 = {}'.format(n, n * 2))
print('{} vezes 3 = {}'.format(n, n * 3), end='   ')
print('{} vezes 4 = {}'.format(n, n * 4))
print('{} vezes 5 = {}'.format(n, n * 5), end='   ')
print('{} vezes 6 = {}'.format(n, n * 6))
print('{} vezes 7 = {}'.format(n, n * 7), end='   ')
print('{} vezes 8 = {}'.format(n, n * 8))
print('{} vezes 9 = {}'.format(n, n * 9), end='   ')
print('{} vezes 10 = {}'.format(n, n * 10))
'''


n = int(input('\033[1;35mDigite um número: '))
print('\033[1;32mAqui está a tubuada deste número: ')
print('{} x {} = {}    {} x {} = {}'.format(n, 1, n * 1, n, 6, n * 6))
print('{} x {} = {}   {} x {} = {}'.format(n, 2, n * 2, n, 7, n * 7))
print('{} x {} = {}   {} x {} = {}'.format(n, 3, n * 3, n, 8, n * 8))
print('{} x {} = {}   {} x {} = {}'.format(n, 4, n * 4, n, 9, n * 9))
print('{} x {} = {}   {} x {} = {}'.format(n, 5, n * 5, n, 10, n * 10))


# consegui!

# certinho