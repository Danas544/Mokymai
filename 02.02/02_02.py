# Create a program which would take 5 separate sentences containing 5 words.
# Make those sentences in separate lists and sort them out (reverse=False)
# Create 5 five new lists what would contain first, second  indexed elements from those lists. (first list containing
# all first elements of those five, second list second elements and so on).
# print the length of all list items and print the longest lenght list and shortest.

pirmas = input("Sakinys is penkiu zodziu: ")
antras = input("Sakinys is penkiu zodziu: ")
trecias = input("Sakinys is penkiu zodziu: ")
ketvirtas = input("Sakinys is penkiu zodziu: ")
penktas = input("Sakinys is penkiu zodziu: ")

listas_pirmas = []
listas_antras = []
listas_trecias = []
listas_ketvirtas = []
listas_penktas = []

# ilgis_pirmo = []
# ilgis_antro = []
# ilgis_trecio = []
# ilgis_ketvirto = []
# ilgis_penkto = []


# ilgis_pirmo.append(len(pirmas))
# ilgis_antro.append(len(antras))
# ilgis_trecio.append(len(trecias))
# ilgis_ketvirto.append(len(ketvirtas))
# ilgis_penkto.append(len(penktas))

listas_pirmas.append(pirmas)
# print(listas_pirmas)
listas_pirmas.append(len(pirmas))
listas_antras.append(antras)
listas_antras.append(len(antras))
listas_trecias.append(trecias)
listas_trecias.append(len(trecias))
listas_ketvirtas.append(ketvirtas)
listas_ketvirtas.append(len(ketvirtas))
listas_penktas.append(penktas)
listas_penktas.append(len(penktas))

bendras = []
bendras.append(listas_pirmas[-1])
bendras.append(listas_antras[-1])
bendras.append(listas_trecias[-1])
bendras.append(listas_ketvirtas[-1])
bendras.append(listas_penktas[-1])

max = max(bendras)
min = min(bendras)

l_max = []
l_min = []

for x in listas_pirmas, listas_antras, listas_trecias, listas_ketvirtas, listas_penktas:
    if x[-1] == max:

        x.remove(x[-1])
        x = str(x).replace("['", '').replace("']", '')
        l_max.append(str(x))


    elif x[-1] == min:

        x.remove(x[-1])
        x = str(x).replace("['", '').replace("']", '')
        l_min.append(str(x))


    else:
        x.remove(x[-1])

print("MAX: ", (l_max))
print("MIN: ", (l_min))


def atvir(kuris_listas):
    atvirksciai = str(kuris_listas)
    # print(type(atvirksciai))
    a = atvirksciai.replace("['", '').replace("']", '')
    a = a.split(" ")
    # print("At: ", a)
    # print(type(a))
    a.reverse()
    return a
    # print('Atvirkščiai: ', a)


for atvirksciai in listas_pirmas, listas_antras, listas_trecias, listas_ketvirtas, listas_penktas:
    print('Atvirkščiai: ', atvir(atvirksciai))

# all first elements of those five, second list second elements and so on).

pirmi_zodziai = []
antri_zodziai = []
treti_zodziai = []
ketvirti_zodziai = []
penkti_zodziai = []


def zodziai(zodis, kuris):
    pirmas_zodis = str(zodis)
    a = pirmas_zodis.replace("['", '').replace("']", '')
    # print(a)
    a = a.split(" ")
    # print(a)
    if len(pirmi_zodziai) != 4:
        a = pirmi_zodziai.append(a[kuris])
    elif len(antri_zodziai) != 4:
        a = antri_zodziai.append(a[kuris])
    elif len(treti_zodziai) != 4:
        a = treti_zodziai.append(a[kuris])
    elif len(ketvirti_zodziai) != 4:
        a = ketvirti_zodziai.append(a[kuris])
    elif len(penkti_zodziai) != 4:
        a = penkti_zodziai.append(a[kuris])
    else:
        a = False

    # print(a)
a = True


while a:
    for a in listas_pirmas, listas_antras, listas_trecias, listas_ketvirtas, listas_penktas:
        if len(pirmi_zodziai) != 4:
            zodziai(a, 0)
        elif len(antri_zodziai) != 4:
            zodziai(a, 1)
        elif len(treti_zodziai) != 4:
            zodziai(a, 2)
        elif len(ketvirti_zodziai) != 4:
            zodziai(a, 3)
        elif len(penkti_zodziai) != 4:
            zodziai(a, 4)
        else:
            a = False


print(pirmi_zodziai)
print(antri_zodziai)
print(treti_zodziai)
print(ketvirti_zodziai)
print(penkti_zodziai)
