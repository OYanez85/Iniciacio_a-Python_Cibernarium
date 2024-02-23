# La cistella de la compra

#Pomes: 3,56 €
#Mandarines: 4,35 €
#Síndria: 6,23 €
#Maduixes: 4,28 €
#Peres: 2,86
#Taronges: 3,48 €

cistella = {
    'Pomes': 3.56,
    'Mandarines': 4.35,
    'Síndria': 6.23,
    'Maduixes': 4.28,
    'Peres': 2.86,
    'Taronges': 3.48
}

# Podries calcular la mitjana de la compra accedint als valors de les claus? Procura posar només dos decimals.
average_price = sum(cistella.values()) / len(cistella)
average_price_formatted = round(average_price, 2)

print(average_price_formatted)


# Podries copiar i guardar en una nova variable la llista dels imports sense tenir en compte els dos últims?
claus=cistella.keys()
claus_llista=list(claus)
print(claus_llista[:4])

valors=cistella.values()
valors_llista=list(valors)
print(valors_llista[:4])


# Podries saber com comprovar si hem comprat llimones?

claus = cistella.keys()
print('llimones' in list(claus))