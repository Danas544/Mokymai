# Parašykite python programą, kuri paprašytų vartotojo įvesti vardą, 
# pavardę, amžių. Įrašykite šias reikšmes į žodyną ir išspausdinkite žodyną


vardas = str(input("vardas: " ))
pavarde = str(input("pavarde: " ))
amzius =  int(input("amzius: " ))

dic = {
    "vardas": vardas,
    "pavarde": pavarde,
    "amzius": amzius
}

print(dic)