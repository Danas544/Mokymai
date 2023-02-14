# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.
# Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.

pirmas , antras = input("Iveskite 2 skaicius per tarpa: ").split(" ")



def sudetis(pirmas: int,antras: int)-> int:
    return pirmas + antras

def aimtis(pirmas: int,antras: int)-> int:
    return pirmas - antras

def dalyba(pirmas: int,antras: int)-> float:
    return pirmas / antras

def daugyba(pirmas: int,antras: int)-> int:
    return pirmas * antras



print(sudetis(int(pirmas),int(antras)))

print(aimtis(int(pirmas),int(antras)))

print(dalyba(int(pirmas),int(antras)))

print(daugyba(int(pirmas),int(antras)))