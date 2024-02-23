#1 FOR. Principalment, hi ha dos cicles: els for i els while
for i in range(10):
    print(i)

#2 En  aquest  exemple,  la  seqüència  comença al3  i  acaba al  9.
for j in range(3,10):
    print(j)

#3
numeros = [5,8,12,24]

for num in numeros:
    print(num)

#4 Aquest exemple ens mostra com podem afegir, de la llista numeros, 
# els valors més grans que 10  en  una  nova  llista  anomenada major10 i, 
# els  valors  més  petits  que  10  en  una  altra  llista anomenada menor10
numeros = [5,8,12,24,13,4,6,11]
major10 = []
menor10 = []

for num in numeros:
    if num > 10:
        major10.append(num)
    else:
        menor10.append(num)

print('major10: ', major10)
print('menor10: ', menor10)

#5 Els  cicles while,  en  lloc  de  repetir  codi  seguint  una  seqüència  iterable,  
# el  que  necessiten  és que una condició sigui verdadera per repetir el codi. 
# Quan la condició deixade ser verdadera, el codi deixa de repetir-se. Vegem-neun exemple senzill:
n = 5
while n < 10:
    print(n)
    n = n + 1

#6 The first snippet prints the initial value of n before incrementing it, while the second snippet increments n first and then prints the updated value.
# Both snippets achieve the same result of printing numbers from 5 to 9, but the order of operations differs.
n = 5
while n < 10:
    n = n + 1
    print(n)

#7 WHILE Aquí anirem repetint el codi fins que trobem el nom Sílvia.
noms = ['Joan', 'Maria', 'Enric', 'Silvia', 'Aleix']
j = 0
trobat = False

while noms[j] != 'Silvia':
    print('Hem trobat la Silvia?', trobat)
    j = j + 1

trobat = True
print('Hem trobat la Silvia?', trobat)
