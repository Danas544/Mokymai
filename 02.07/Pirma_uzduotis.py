# Leiskite naudotojui įvesti vardą, pavardę ir amžių. Išspausdinkite,
#  ar naudotojas gali įeiti į internetinį kazino, ar ne. 21 metai yra amžiaus riba.



vardas = str(input("Vardas: "))
pavarde = str(input("Pavarde: "))
amzius = int(input("Amžius: "))

c = 21

if amzius >= c:
    print(f'Sveiki atvyke į kazino {vardas} {pavarde}')
else:
    skirtumas = c - amzius
    if skirtumas < 10:
         print(f'Atsiprašau {vardas} {pavarde} jums reikia dar palaukti {skirtumas} metus')
    else:
        print(f'Atsiprašau {vardas} {pavarde} jums reikia dar palaukti {skirtumas} metų')



