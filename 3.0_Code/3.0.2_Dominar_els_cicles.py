#1
for i in range(10):
    print(i)

#2
for j in range(3,10):
    print(j)

#3
numeros = [5,8,12,24]

for num in numeros:
    print(num)

#4
numeros = [5,8,12,24,13,4,6,11]
major10 = []
menor10 = []

#5
for num in numeros:
    if num > 10:
        major10.append(num)
    else:
        menor10.append(num)

print('major10: ', major10)
print('menor10: ', menor10)

#6
n = 5
while n < 10:
    print(n)
    n = n + 1

#7
n = 5
while n < 10:
    n = n + 1
    print(n

#8
noms = ['Joan', 'Maria', 'Enric', 'Silvia', 'Aleix']
j = 0
trobat = False

while noms[j] != 'Silvia':
    print(Hemtrobat la Silvia?', trobat)
    j = j + 1

trobat = True
print('Hem trobat la Silvia?', trobat)
