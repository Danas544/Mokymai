# Sukurkite Python listą su įvairiausiais objektais,
#  juo daugiau tuo geriau.
#  Išspausdinkite visus tipus. Tas, kuris surinks daugiausiai unikalių tipų, laimi pagarbos taškų:


listas = [1.111,2.321,5.567,778.784919,111222.8949,147.963]

apvalinti = []

for x in listas:
    x = round(x,2)
    apvalinti.append(x)
print(listas)
print("FOR x in apvalina: ", apvalinti)

ilgis = len(listas)
#print(ilgis)
while_apvalina = []
x = 0
while ilgis >= x :
    if ilgis != x:
       a = listas[x]
       a = round(a,2)
       #print(a)
       while_apvalina.append(a)
       x += 1
    else:
        break
print('WHILE apvalina: ' , while_apvalina)