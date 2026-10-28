import random
a1 = input('Nome do primero aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do último aluno: ')
l = [a1, a2, a3, a4]
a = random.choice(l)
print('O aluno sorteado para apagar o quadro '
      'foi {}'.format(a))


# certinho. Segui o mesmo raciocínio da lista e do random.choice
