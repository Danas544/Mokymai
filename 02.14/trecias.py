# Create a function that returns only strings with unique characters.
# Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias eilutes.

zodis = str(input("Sakinys: "))

def unikalus(txt: str)-> str:
    a = set(txt)
    return str(a)

print(unikalus(zodis))