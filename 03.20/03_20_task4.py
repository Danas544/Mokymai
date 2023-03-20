# Sukurkite skaičiuotuvo programą: joje turėtų būti abstrakti klasė su metodais (abstrakčiais ir neabstrakčiais), bazinė klasė,
# geometrijos, aritmetinis skaičiuotuvas klases. Kiekviena poklasė turėtų turėti bent 5 metodus, kad būtų galima atlikti keletą prasmingų skaičiavimo operacijų.

# Create a Calculator program : it should contain abstract class with methods (abstract and not),
#  base class, geometry, arithmetic calculator classes. Every subclass should have at least 5 methods to make some meaningful calculus operations.
from abc import ABC, abstractmethod
from typing import Union


class Calculator(ABC):
    def __init__(self, tekstas: str) -> None:
        self.tekstas = tekstas


    def tvarkom_teksta(self) -> str:
        split = self.tekstas.split(" ")
        self.sk1 = float(split[0])
        self.sk2 = float(split[2])
        self.salyga = split[1]
        return self.salyga


class Base(Calculator):
    def __init__(self, tekstas: str) -> None:
        super().__init__(tekstas)



    def sudetis(self) -> float:
        return self.sk1 + self.sk2

    def atimtis(self) -> float:
        return self.sk1 - self.sk2

    def daugyba(self) -> float:
        return self.sk1 * self.sk2

    def dalyba(self) -> Union[int,str]:
        try:
            return self.sk1 / self.sk2
        except ZeroDivisionError:
            return "Dalyba iš 0 negalima"


class Geometry(Calculator):
    def __init__(self, tekstas: str) -> None:
        super().__init__(tekstas)



start = True
while start is True:
    try:
        print("Ka darysime? 1. Base calculator 2. Geometry calculator")
        pasirinkimas = int(input())
        start = False
    except ValueError:
        print("Blogas pasirinkimas seniuk :/")

if pasirinkimas == 1:
    cal = Base(input("Base calculator: "))
    if cal.tvarkom_teksta() == "+":
        print(cal.sudetis())
    elif cal.tvarkom_teksta() == "-":
        print(cal.atimtis())
    elif cal.tvarkom_teksta() == "*":
        print(cal.daugyba())
    elif cal.tvarkom_teksta() == "/":
        print(cal.dalyba())
elif pasirinkimas == 2:
    print("Reikia antro")
