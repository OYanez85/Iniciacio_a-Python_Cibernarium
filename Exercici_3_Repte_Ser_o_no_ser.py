# Ara et toca a tu: Repte. Ser o no ser
# Genera una seqüència iterable formada per una llista de 10 números enters majors que 0 i menors que 20. 
# Procura que tots els números d’aquesta llista els entris per teclat. Una vegada tinguis la llista, realitza les accions següents:

# Fes que tots els elements siguin multiplicats per 3, si són menors que 10, o per 2, si són majors que 10. Fes ús de l’estructura for.
# Imprimeix la llista. Fes ús de l’estructura for.
# A continuació, imprimeix només els cinc primers números. Fes ús de l’estructura while.
 

# Si vols, i de manera opcional, intenta fer aquest últim pas:

# Torna a fer les accions anteriors, però en lloc d’introduir els números per teclat, fes-ho important el mòdul random 
# i fent ús de la funció randint().

#num = int(input())

numeros = [5,8,12,2,13,4,6,11,19,15]
major10 = []
menor10 = []

for num in numeros:
    if num > 10:
        major10.append(num * 2)
    elif num < 10:
        menor10.append(num * 3)

print('major10: ', major10)
print('menor10: ', menor10)