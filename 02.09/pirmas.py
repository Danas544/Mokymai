# Sukurkite kintamuosius, kuriuose būtų vartotojo vardo ir slaptažodžio stringai. Pradėkite begalinį ciklą, leidžiantį įvesti vartotojo vardą ir slaptažodį.
#  Jei duomenys teisingi, sustabdykite begalinį ciklą ir išspausdinkite pasisveikinimo pranešimą.


username = 'Danielius'
password = '147'

while True:
    user , passw = input("username and password: ").split()
    #passw = input("password: ")
    if passw == password and username == user:
        print("Sveiki atvyke")
        break
    else:
        print("Blogi prisijungimai")
        
