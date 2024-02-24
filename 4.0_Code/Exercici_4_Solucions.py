# Ara et toca a tu: Repte. Fes-ho una vegada i crida-la tantes vegades com vulguis
# A continuació, et proposem resoldre un exercici vinculat a les funcions.

#Suposem que tenim una col·lecció de números enters guardats en una llista. 
# Construeix una funció que agafi com a paràmetre aquesta llista i que torni una nova llista els valors de la qual siguin el doble de la llista d’entrada.

#Per exemple, si el paràmetre de la funció és [4,6,8], el retorn serà [8,12,16].

#Construeix una nova funció (que anomenarem funcio_1) que agafi com a paràmetre i que, primer, multipliqui per 3 els seus valors, si aquests no són superiors a 10 i, després, que imprimeixi la llista. 
# Invoca aquesta funció de tal manera que el valor del seu paràmetre sigui la llista que torni la primera funció.  

#Resol l’exercici per aquestes tres llistes diferents que agafen la funcio_1 com a paràmetre:

#[4,5,7]

#[1,3,2]

#[3,6,8]

#Procura resoldre l’exercici suposant que la llista que agafa com a paràmetre la funcio_1 és una seqüencia de quatre valors enters generats aleatòriament de l’1 al 9.

# 1.
seq = [4,5,7]

def funcio_1(llista):
    for i in range(len(llista)):
        llista[i] = llista[i] * 2
        
        return llista

def funcio_2(llista):
    for i in range(len(llista)):
        if llista[i] <= 10:
            llista[i] = llista[i] * 3
    print(llista)
    
funcio_2(funcio_1(seq))

# 2.
import random

def funcio_1(llista):
    for i in range(len(llista)):
        llista[i] = llista[i] * 2
        
    return llista

def funcio_2(llista):
    for i in range(len(llista)):
        if llista[i] <= 10:
            llista[i] = llista[i] * 3
        print(llista)

def llista_aleatoria(n):
    llista = []
    for i in range(n):
        llista.append(random.randint(1,9))
    print('llista aleatoria: ', llista)
    return llista

funcio_2(funcio_1(llista_aleatoria(4)))