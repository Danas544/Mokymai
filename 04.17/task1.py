# 1: Create a generator function that takes a positive integer n as input and generates all the even numbers up to and including n.

# sukurkite generatoriaus funkciją, kuri kaip įvestį paima teigiamą sveikąjį skaičių n ir generuoja visus lyginius skaičius iki n imtinai.

from collections.abc import Iterator

def generate_positive_number(number:int) -> Iterator[int]:
        for x in range(number+1):
            if x % 2 == 0:
                yield x




gen = generate_positive_number(10)

for x in gen:
    print(x)
# try:
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))
# except StopIteration:
#     pass
