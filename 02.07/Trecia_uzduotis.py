# allow user to enter two numbers, print out which one is higher than the other, or are they equal?
# Leiskite naudotojui įvesti du skaičius, išspausdinkite, kuris iš jų didesnis už kitą, ar jie lygūs?


pirmas_sk = int(input("Pirmas sk: ")) 
antras_sk = int(input("Antras sk: ")) 

if pirmas_sk == antras_sk:
    print(f"Skaiciai lygus")
elif(pirmas_sk > antras_sk):
    print(f"Pirmas skaičius didesnis až antra skaiciu")
elif(pirmas_sk < antras_sk):
    print(f"Antras skaičius didesnis už pirma skaiciu")
else:
    print("error")