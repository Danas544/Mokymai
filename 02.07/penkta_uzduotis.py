# Sukurkite skaičių nuo 1 iki 10 spėjimo žaidimą su atsitiktinių skaičių biblioteka. (GALBŪT IDĖJA VĖLESNIAM LAIKUI)


# create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)
import random

while True:
    r = random.randint(1,10)
    try:
        sk = int(input("Spek skaičiu: "))
    except:
        sk = int(input("Turi dar viena šansa įvesti skaičiu: "))
    if sk == r:
        print(f"Atspėjai {sk}!!!")
    else:
        print(f"Gaila , bet ne atspėjai skaičius buvo {r}")
    dar = input("Žaidžiam dar? (y/n): ")
    if dar == "n":
        print("Ačiū , kad žaidei")
        break
