# Sukurkite programą su 3 skirtingais moduliais:

# Pirma, atlikti pagrindines užduotis su eilutėmis
# antra, pagrindinius uždavinius su sąrašais.
# trečias, pagrindiniai uždaviniai su skaičiais
# Importuokite juos kaip modulius į main.py modulį ir parodykite skaičiavimus.

# Create a program with 3 different modules:

# first, to do basic tasks with strings
# second, basic tasks with lists.
# third, basic tasks with numbers
# Import them as modules to the main.py module and show calculations.
from antras_modul_checkinput import check_input
from antras_modul_string import string_add
from antras_modul_list import add_lists
from antras_modul_number import add


print("Sujungiam 2 tekstus")
pirmas = input("Rašom: ")
antras = input("Rašom dar karta: ")
patik_pirmas , patik_antras = check_input(pirmas,antras)
print(string_add(patik_pirmas,patik_antras))


print("Sujungiam listus")
list1 = [1,2,3,4]
list2 = [5,6,7,8,9,10]
print(add_lists(list1,list2))

print("Sudedam du skačius")
sk1 = input("Rašom sk: ")
sk2 = input("Rašom sk dar karta: ")
patik_sk1, patik_sk2 = check_input(sk1,sk2)
print(add(patik_sk1,patik_sk2))


