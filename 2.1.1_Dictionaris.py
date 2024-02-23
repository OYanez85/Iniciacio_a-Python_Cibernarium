samarretes = {'vermelles': 1, 'blanques': 5, 'blaves': 2, 'negres': 3}

claus = samarretes.keys()
print('grogues' in list(claus))

samarretes['grogues'] = 1

claus = samarretes.keys()
print('grogues' in list(claus))

print(list(claus).index('grogues'))

valor_llista = list(samarretes.values())
print(sum(valor_llista))

