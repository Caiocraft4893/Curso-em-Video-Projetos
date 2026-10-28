from random import shuffle
n1 = input('Primeiro aluno a apresentar o trabalho: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('último aluno: ')
l = [n1, n2, n3, n4]
shuffle(l)  # ---> usado para embaralhar algo. não precisa atribuir
print('A ordem ficou assim: ')                # a uma variável
print(l)
#    ^
'''  ^
Aqui eu dou o print (exibo na tela) a lista já embaralhada (os 
elementos)
'''

# precisei da correção.

'''
O meu erro foi ter atribuído o shuflle a uma variável e usado
o .format, como na maioria dos programas feitos até agora.
'''
