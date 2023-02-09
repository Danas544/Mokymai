# Sugeneruokite 10 raktų žodyną: 1,2,3...10.
#  Kiekviename iš jų turėtų būti įrašyta atsitiktinio sveikojo skaičiaus vertė nuo 1 iki 100.


# Generate a dictionary of 10 keys being 1,2,3...10 
# each of them should store a value of random integer number from 1 to 100.
import random
dictionary = {
"pirmas": random.randint(1,100),
"antras": random.randint(1,100),
"trecias": random.randint(1,100),
"ketvirtas": random.randint(1,100),
"penktas": random.randint(1,100),
"sestas": random.randint(1,100),
"septintas": random.randint(1,100),
"astuntas": random.randint(1,100),
"devintas": random.randint(1,100),
"desimtas": random.randint(1,100)
}

print(dictionary)

