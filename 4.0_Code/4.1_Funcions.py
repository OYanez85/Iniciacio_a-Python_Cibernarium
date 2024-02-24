# Funcions

# 1 Aquesta funció s’encarrega d’imprimir el doble de x.
def duplicar(x):
    y = x * 2
    print (y)
    
# 2 Per  tal  que s’executi el codi de la funció, cal invocar-la. Per fer-ho, només caldrà escriure:
duplicar(5)

# 3 La  funció encadenar_paraules()afegeix el valor del seu paràmetre a la llista majors_cinco menors_igual_cinc, depenent de si aquest  és  major  que  5  o  no.  
# Per  tal  de  no  haver  de  repetir  els  condicionals  i  les  funcions append()durant el cicle while, dissenyem primer la funció i després només cal invocar-la dins del  bloc while.

majors_cinc = []
menors_igual_cinc = []
repliques = 0

def encadenar_paraules(num):
    if num > 5:
        majors_cinc.append(num)
    else:
        menors_igual_cinc.append(num)

while repliques < 5:
    print('introdueix número')
    encadenar_paraules(int(input()))
    repliques += 1
    
print('número rèpliques és', str(repliques))
print('numeros majors 5', majors_cinc)

# 4 Tot seguit, redactarem una funció que sigui capaç de tornar un valor. Això voldrà dir que, cada vegada  que  executem  la  funció,  aquesta  podrà  emetre  un  resultat.  
# La  manera  que  té  una funció de generar un resultat és mitjançant la sentència return.
def duplicar(x):
    return x * 2
y = duplicar(3)

print(y)

# 5 La variable zés la suma de la variable y,  és  a  dir  5,  i  la  del  valor  que  genera  la  funció  duplicar,  és  a  dir  6.  
# El  resultat  de  l’operació, doncs, és 5 + 6.
def duplicar(x):
    return x * 2
y = 5
z = y+ duplicar(3)
print(z)

#6 Les  funcions  poden  generar  qualsevol  tipus  d’objecte.  Per  exemple,  també  podem  generaruna llista

a = [4,2,7]
b = [6,3,12]

def llista_doble(llista):
    nova_llista = []
    for i in range(len(llista)):
        nova_llista.append(llista[i] * 2)
    return nova_llista

print(llista_doble(a))
print(llista_doble(b))