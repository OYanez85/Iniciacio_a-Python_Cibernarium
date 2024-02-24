#1. 
def llista():
    return [4,6,8]

def operacio_1(a):
    return [i * 2 for i in a]
a=llista()

print(operacio_1(a))

# 2.
import random

# Funció per duplicar els valors de la llista
def duplicar(valors):
    return [x * 2 for x in valors]

# Funció que multiplica per 3 els valors <= 10, i imprimeix la llista
def funcio_1(valors):
    valors = [x * 3 if x <= 10 else x for x in valors]
    print(valors)

# Llistes d'entrada
llistes = [
    [4, 5, 7],
    [1, 3, 2],
    [3, 6, 8]
]

# Processar cada llista a través de les funcions definides
for llista in llistes:
    llista_duplicada = duplicar(llista)
    print(f"Llista original duplicada: {llista_duplicada}")
    funcio_1(llista_duplicada)

# Generar una llista de quatre valors enters aleatòriament entre 1 i 9
llista_aleatoria = [random.randint(1, 9) for _ in range(4)]
print(f"Llista aleatòria: {llista_aleatoria}")
llista_aleatoria_duplicada = duplicar(llista_aleatoria)
print(f"Llista aleatòria duplicada: {llista_aleatoria_duplicada}")
funcio_1(llista_aleatoria_duplicada)
