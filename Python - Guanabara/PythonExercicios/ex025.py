n = input('Qual o seu nome? ')
m = n.upper()
print('Vamos ver se tem "Silva" no seu nome:')
v = 'SILVA' in m
print(v)


# Esse exercício é diferente do 24, que tinha que começar com "santo",
# nesse pode ter "silva' em qualquer lugar do nome.

# certinho, mas eu poderia também resolver dessa forma:

'''
nome = str(input('Qual é o seu nome completo? '))
print('Seu nome tem Silva? {}'.format('silva' in nome.upper()))
                                               ^>------^
                                               |
O nome.upper() joga toda maneira de escrever "silva" para 
maiúscula. 
'''