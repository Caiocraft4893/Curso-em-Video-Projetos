d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
p = d * 60
r = km * 0.15
t = p + r
print('O total a pagar é R${:.2f}'.format(t))

# certinho (mas precisei ver o enunciado no video de correção)