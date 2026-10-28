# Meu jeito:

'''
f = str(input('Escreva uma frase: ')).strip()
m = f.lower()
c = m.count('a')
e = len(m[0])
e2 = m.rfind('a')
print('Sua frase tem: {} letras "a",\no primeiro "a" começou na '
      'posição {} \ne ela termina na posição {}'.format(c, e, e2))
'''

# não consegui fazer a última (linha 6/7).

# Jeito do guanabara:

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A úlima letra A apareceu na posição {}'.format(frase.rfind('A')+1))

'''
Eu errei porque não tinha conhecimento desse "+1", visto que o 
python começa a contar as strings a partir do número 0, mas 
a gente conta a partir do 1, por isso o +1. 
Mas fora isso, o raciocínio foi o mesmo.

Posso começar também a usar as funcionalidades dentro do .format(),
e não as atribuírem a uma variável.
'''




