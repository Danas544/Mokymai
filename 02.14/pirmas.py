# Create a function that adds a string ending to each member in a list.
# Sukurkite funkciją, kuri prie kiekvieno sąrašo nario prideda eilutės galūnę.


listas = ["Danielius","Petras",'Jonas']

def adds_strint_to_end(txt: str):
    listas.append(txt)


adds_strint_to_end("Maryte")
print(listas)




def add_to_each_member(listukas) -> list:
    new_list = []
    last = listas[-1]
    for x in listas:
        new_list.append(x+' + '+last)
        #new_list.append(last)
    return new_list

a = add_to_each_member(listas)
print(a)
