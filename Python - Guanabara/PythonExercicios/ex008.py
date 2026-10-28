n = float(input('\033[1;34mQuantos metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('\033[1;33m{} metros corresponde a \n {}km \n {}hm \n {}dam '
      '\n {:.0f}dm \n {:.0f}cm \n {:.0f}mm'
      ''.format(n, km, hm, dam, dm, cm, mm))

# certinho