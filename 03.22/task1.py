# Užduotis Nr.1 Sukurkite .envfailą su aplinkos kintamaisiais:
# Vartotojo vardas
# Slaptažodis
# Parašykite programą, prašydami vartotojo įvesti usernameir password. Patikrinkite, ar vartotojas įvedė tuos pačius kredencialus kaip ir jūsų .env faile.
# Jei taip, spausdinkite "PRIEIGA SUTEIKTA" Priešingu atveju spausdinkite "WRONG CEDENTIALS", kol vartotojas neįves teisingos informacijos.


from dotenv import dotenv_values

config = dotenv_values(".env")

username = input("UserName: ")
password = input("Password: ")


if config["env_username"] == username and config["env_password"] == password:
    print("PRIEIGA SUTEIKTA")
else:
    print("BLOGI PRISIJUNGIMAI")
