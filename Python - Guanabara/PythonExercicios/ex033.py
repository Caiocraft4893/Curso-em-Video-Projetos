'''
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
if n1 > n2 > n3:
    print('{} é o maior número'.format(n1))
    print('{} é o menor número.'.format(n3))
if n1 > n3 > n2:
    print('{} é o maior número'.format(n1))
    print('{} é o menor número'.format(n2))
if n2 > n1 > n3:
    print('{} é o maior número'.format(n2))
    print('{} é o menor número'.format(n3))
if n2 > n3 > n1:
    print('{} é o maior número'.format(n2))
    print('{} é o menor número'.format(n1))
if n3 > n2 > n1:
    print('{} é o maior número'.format(n3))
    print('{} é o menor número'.format(n1))
# agora, para casos iguais.
if n1 == n2 > n3:
    print('{} é o maior número'.format(n1))
    print('{} é o menor número'.format(n3))
if n1 == n3 > n2:
    print('{} é o maior número'.format(n1))
    print('{} é o menor número'.format(n2))
if n2 == n3 > n1:
    print('{} é o maior número'.format(n2))
    print('{} é o menor número'.format(n1))
if n1 == n2 == n3:
    print('Os três números são iguais. Não há maior nem menor.')
'''
# Meu jeito

# Jeito do Guanabara

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verficando quem é o menor
menor = a  # ---> Eliminamos 1 if, a necessidade de testar se a é o menor
if b<a and b<c:       # considerando ele já como o menor!
    menor = b       # E se os outros forem menor, o menor será substituído
if c<a and c<b:                                         # por eles.
    menor = c  #---> Isso é, se c for menor que a e b, c é menor (recebe menor).
# Verificando quem é maior
maior = a
if b>a and b>c:
    maior = b  # --> Se b for maior que a e c, b é o maior (passa a ser "maior")
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

# Visto que não há problema em fazer da forma que fiz, tudo certinho,
# detalhadinho, manualmente. Só que fiz errado.


# O exercício é melhor que a aula. O exercício é mais importante. -Guanabara.