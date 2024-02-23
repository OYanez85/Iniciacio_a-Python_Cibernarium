temp = int(input())
prob = float(input())

dic = {'jaqueta}: False, 'pantalons': 'curts', 'calçat': 'normal'}

if temp <= 20:
    dic['jaqueta'] = True
    dic['pantalons'] = 'llargs'
    if prob > 75:
        dic['calçat'] = 'hivern'
elif temp > 20:
    if prob > 80:
        dic['calçat'] = 'botes d\'aigua' 
        
print(dic)