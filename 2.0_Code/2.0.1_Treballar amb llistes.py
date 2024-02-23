# Treballar amb llistes

llista_enters = [4,6,3,7,8]

llista_mixta = [-4, 7.8, 'hola', False]

a = llista_enters[0]
b = llista_mixta [3]

print(llista_mixta[2])

# Per  exemple,  si  volem extreure  de llista_mixtala  dada 7.8,  ho  podem  fer  d’aquestes  dues maneres:
a = llista_mixta[1]
b = llista_mixta[-3]

print(len(llista_enters))

#Afegir una nova dada –append()
llista_mixta.append(True)

#Extreure l’última dada –pop()
llista_enters.pop()
print(llista_enters)

#Identificar la posició d’una dada –index():
print(llista_mixta.index('hola'))

#Fer una còpia d’una llista,seleccionant només certes posicions
a = llista_enters[0:3]

notes_alumnes = [8.75, 3.50, 5.50, 6.25, 9.75, 2.75, 4.50, 7.60]
notes_ultimes = notes_alumnes[3:]

notes_ultimes = notes_alumnes[:5]

