i = 0
while i < 10:
  print(i)
  i += 1

while True:
    user_input = input("Įveskite savo vardą: ")
    if len(user_input) != 0:
        break
print(f"Jūs įvedėte {user_input }")