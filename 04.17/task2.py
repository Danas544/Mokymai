# Create a generator function that would pick word from a generator and/list of generated random words (should be > 10000) and would stop itterating
# until the word longer than 7 lettters is found.
# Compare sizes of list and generator. Calculate performance per both executions (time to complete in ms)

# Sukurkite generatoriaus funkciją, kuri pasirinktų žodį iš generatoriaus ir (turėtų būti > 10000) sugeneruotų atsitiktinių žodžių sąrašo ir nustotų kartoti
# kol bus rastas žodis ilgesnis nei 7 raidės.
# Palyginkite sąrašo ir generatoriaus dydžius. Apskaičiuokite abiejų vykdymų našumą (užbaigimo laikas ms)
import time
import sys
import datetime
from collections.abc import Iterator
from py_random_words import RandomWords
r = RandomWords()

random_words_list = [r.get_word() for  x in range(10000)]
print(f"random_words_list: {sys.getsizeof(random_words_list)}")

random_words_gen = (x for  x in random_words_list)

print(f"random_words_gen: {sys.getsizeof(random_words_gen)}")


def generator(random_words) -> Iterator[int]:    
    for x in random_words:
        if len(x) < 6:
            yield x
        else:
            break

pradzia = datetime.datetime.today()
gen = generator(random_words_list)
for x in gen:
    print(x)
pabaiga = datetime.datetime.today()
print(f"random_words_list Programa užtruko {(pabaiga - pradzia)}")

gen = generator(random_words_gen)
for x in gen:
    print(x)
pabaiga = datetime.datetime.today()
print(f"random_words_gen Programa užtruko {(pabaiga - pradzia)}")