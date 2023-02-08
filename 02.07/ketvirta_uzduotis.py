# Parašykite nedidelę skaičiuotuvo programą, kuri leistų naudotojui įvesti du skaičius ir simbolį,
#  duotą ir tada atlikti operaciją bei išspausdinti atsakymą.


# Write a small calculator application, that allows user to enter two numbers
#  and a symbol, given and then do the operation and print an answer.

# sk1 = int(input('Pirmas skaicius: '))
# sym = input('Simbolis: ')
# sk2 = int(input('Antras skaicius: '))


# if sym == "+":
#    ats = sk1 + sk2
#    print(ats)
# elif(sym == "-"):
#     ats = sk1 - sk2
#     print(ats)
# elif(sym == "*"):
#     ats = sk1 * sk2
#     print(ats)
# elif(sym == "/"):
#     ats = sk1 / sk2
#     print(ats)
# elif(sym == "**"):
#     ats = sk1 ** sk2
#     print(ats)
# else:
#     print("sugedo skaičiuotuvas")



sk1 , sym, sk2 = input('Pirmas skaicius: ').split()

sk1 = int(sk1)
sk2 = int(sk2)
sym_list = ["+","-","*","/","**"]
if sym in sym_list:

    if sym == "+":
        ats = sk1 + sk2
    elif(sym == "-"):
        ats = sk1 - sk2
    elif(sym == "*"):
        ats = sk1 * sk2
    elif(sym == "/"):
        ats = sk1 / sk2
    elif(sym == "**"):
        ats = sk1 ** sk2
else:
    print("sugedo skaičiuotuvas")
print(ats)