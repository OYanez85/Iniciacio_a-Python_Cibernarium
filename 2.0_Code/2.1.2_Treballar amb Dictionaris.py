# Treballar amb Dictionaris

notes_dict={'Joan':4.85,'Miquel':7.80,'Meritxell':8.15,'Laura':4.75}

#  mètode dict
notes_dict=dict(Joan=4.85,Miquel=7.80,Meritxell=8.15,Laura=4.75)

#Si volem accedir, per exemple,  a la nota de la Meritxell i guardar-la en una variable,ho farem així:
nota_meritxell=notes_dict['Meritxell']

# També podem accedir al valor d’una clau determinada fent ús de la funció get()
notes_dict.get('Laura')

# Si volem afegir una nova parella clau-valor,només haurem d’escriure aquesta sentència
notes_dict['Eduard']=6.80

# Per saber el número de clau-valor que conté un diccionari funció len()
print(len(notes_dict))

# Si volem, per exemple, extreure la col·lecció de claus en forma de llista, ho podem fer amb dos passos La funció keys() 
claus=notes_dict.keys()
claus_llista=list(claus)

# Ho farem de la mateixa manera que amb les claus,però en lloc de fer-ho cridant la funció keys(), cridarem la funció values()
valors=notes_dict.values()
valors_llista=list(valors)

# Això ens pot servir,per exemple,per saber si una clau es troba en un diccionari o no. Per saber si hi és o no,ho farem així
print('Kim'inclaus_llista)

# I, si per alguna raó ens interessa generar una llista amb les parelles clau-valor, ho podrem fer cridant la funció items().
parelles=notes_dict.items()
parelles_llista=list(parelles)

# Per tal d’eliminar una parella clau-valor del diccionari
delnotes_dict['Joan']

# Un diccionari pot tenir una clau que el seu valor sigui un altre diccionari. Exemple:
nested_dict={'a':1,'b':2,'c':{'c1':3,'c2':4},'d':5}

# Una llista també pot ser un valor d’una clau d’un diccionari
nested_dict={'a':1,'b':2,'c':[3,4,5,6],'d':7}

#Si volem accedir i imprimir el valor a la posició 2 de la llista, que és el valor de la clau‘c’,
print(nested_dict['c'][2])
