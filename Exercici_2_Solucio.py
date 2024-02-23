compra = {'pomes': 3.56, 'mandarines': 4.35, 'sindria': 6.23, 'maduixes': 4.28, 'peres': 2.86, 'taronges': 3.48}

valors = list(compra.values())
mitjana = sum(valors)/len(valors)

print('La mitjana de la compra es {:.2f}'.format(mitjana))

nou_valors = valors[:-2]
print(nou_valors)

print('llimones' in list(compra.keys())

print('Entra la nova fruita: ')
fruita = input()
print(fruita in list(compra.keys()))