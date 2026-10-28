n = input('\033[1;35mDigite algo: ')
print('Seu tipo é', type(n))
print('\033[1;34mSó tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em maiúscula?', n.isupper())
print('Está em minúscula?', n.islower())
print('Está capitalizada?', n.istitle())

# title = "capitalizada"

# certinho