# Sukurkite duomenų bazę (privilegijuotų naudotojų sąrašas) išspausdinkite konkretų pranešimą su asmeniniu pasveikinimu,
#  jei naudotojas yra privilegijuotas, tik "Sveiki atvykę" kitu atveju.


# Create a database (List of privileged users)
#  print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

sarasas = {
    
    "zmones": [{
            "vardas": "Danielius",
            "privilegija": True
            },
    {
            "vardas": "Antose",
            "privilegija": True
    },
    {
            "vardas": "Jonas",
            "privilegija": False
    },
    {
            "vardas": "Inga",
            "privilegija": False
    }]
    
}

for x in sarasas["zmones"]:
    if x["privilegija"] == True:
        vardas = x["vardas"]
        print(f"Sveiki atvyke {vardas}")
    else:
        vardas = x["vardas"]
        print(f"Šiandien ne dirbam {vardas}")



# if sarasas["zmones"][0]["privilegija"] == True:
#     vardas = sarasas["zmones"][0]["vardas"]
#     print(f"Sveiki atvyke {vardas}")
# else:
#     vardas = sarasas["vardas"]
#     print(f"Šiandien ne dirbam {vardas}")