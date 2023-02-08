try:
    vardas = str(input("Tavo vardas?"))
except:
    print("Tik raidės")
    vardas = str(input("Tavo vardas? TIK RAIDES!!!"))
try:
    metai = int(input("Tavo metai?"))
except:
    print("Tik skaiciai gali būti")
    metai = int(input("Tavo metai? TIK SKAICIAI!!!"))
try:
    data = int(input("Kokie dabar metai?"))
except:
    print("Tik skaiciai gali būti")
    data = int(input("Kokie dabar metai? TIK SKAICIAI!!!!"))
    
a = data - metai
b = a - 1

print(f"Tavo vardas yra {vardas}, tau metu {metai}, gimei {a}, o jei dar bus gimtadienis šiais metais tada gimei {b}  ")
