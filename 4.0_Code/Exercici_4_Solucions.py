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

funcio_2(funcio_1(llista_aletoria(4)))