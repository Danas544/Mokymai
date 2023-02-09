# Leiskite naudotojui įvesti 10 sveikųjų skaičių, tada spausdinkite šių įvestų skaičių sumą ir vidurkį.
import numpy


while True:
    numbers = input("įvesti 10 sveikųjų skaičių: ").split()
    sumuoti = []
    for number in numbers:
        try:
            x = int(number)
            sumuoti.append(x)
        except:
            pass 
    if len(sumuoti) == 10:
        print(sum(sumuoti))
        print(numpy.average(sumuoti))
        break
    else:
        pass
         







# print(sum(sumuoti))
# print(numpy.average(sumuoti))