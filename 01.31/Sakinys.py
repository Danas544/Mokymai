sakinys = input("Tekstas?")

print(sakinys[::-1])
print(sakinys[::2])

s = sakinys.split()

try:
    print(f"Mano vardas: {s[0]} pavarde {s[1]}")
except:
    print(sakinys)


