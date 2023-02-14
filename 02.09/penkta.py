# Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and letters)
# Then count how many each letters are in those words.
# Return answer as a dictionary. {'letter': count}
# And all words sorted in one list.
# 5 lists with 5 word 15 letters random
from random_word import RandomWords
import collections
pirmas = []
antras = []
trecias = []
ketvirtas = []
penktas = []
bendras = []
def random_word():
    r = RandomWords()
    r = r.get_random_word()
    return r

for _ in range(0,5):
    pirmas.append(random_word())
    antras.append(random_word())
    trecias.append(random_word())
    ketvirtas.append(random_word())
    penktas.append(random_word())

bendras.extend(pirmas)
bendras.extend(antras)
bendras.extend(trecias)
bendras.extend(ketvirtas)
bendras.extend(penktas)
#print(bendras)
dictk = []
for bend in bendras:
    x = bend
    dictk.append(x)
    
    
print(dictk)
x = collections.Counter(str(dictk))
print(x)
# for pirm in pirmas:
#     x = pirm
#     p = collections.Counter(x)

# for ant in antras:
#     x = ant
#     a = collections.Counter(x)

# for tre in trecias:
#     x = tre
#     t = collections.Counter(x)

# for ket in ketvirtas:
#     x = ket
#     k = collections.Counter(x)
# for penk in penktas:
#     x = penk
#     pe = collections.Counter(x)

# print(p)
# print(a)
# print(t)
# print(k)
# print(pe)




#print(collections.Counter(x))





