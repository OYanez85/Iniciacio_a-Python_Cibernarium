c1 = 356.75
c2 = 487.45
c3 = 295.83
c4 = 532.00
print('Introdueix canvi:')
canvi = input() #canvi dollars to euros
canvi = float(canvi)

suma_euros = (c1 + c2 + c3 +c4) *canvi
mitjana = suma_euros / 4

print('Suma de les compres {:.2f} euros'.format(suma_euros))
print('Mitjana de les compres: {:.2f} euros'.format(mitjana))

suma_euros_2 =(c1 + c2 + c3 + c4*0.8) * canvi
mitjana_2 = suma_euros_2 / 4

print('Nova suma: {:.2f}'.format(suma_euros_2))
print('Nova Mitjana de les compres: {:.2f} euros'.format(mitjana_2))

suma_type = type(suma_euros)
suma_string = str(suma_euros)
