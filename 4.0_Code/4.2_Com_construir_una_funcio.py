# 1.
def intercanvi_coordenades(x,y,z):
    j = x
    x = y
    y = z
    z = j
    print('x: ', x, 'y:', y, 'z:', j)

intercanvi_coordenades(4,7,9)

# 2. 
def operacio_1(x):
    return x*3 + 6

print(operacio_1(6))

def operacio_2(x):
    return x/3 - 6

print(operacio_2(operacio_1(6)))

# 3. Guradar funcio en una variable f i la invoquem 
f = operacio_1
print(f(4))