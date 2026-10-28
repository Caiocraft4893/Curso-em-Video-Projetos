n = int(input('\033[1;31mDigite um número: '))
print('\033[1;37mO dobro desse número é {}, seu triplo {} '
      'e raiz quadrada {:.2f}'.format(n * 2, n * 3, n **(1/2)))


'''
Aqui eu "quebrei" a linha do código, mas para caber na tela, mas
isso não afeta o resultado (no caso, a mensagem do print) porque 
não utiizei o \n. Fiz só para ficar mais organizado.
'''

# certinho