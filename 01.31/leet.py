
#a = input("Tekstas?")

#leet = {'a':'4','e':'3','i':'1','o':'0','A':'4','E':'3','I':'1','O':'0','d':'|>','n':"|\|",'u':'|_|','s':'5'}

#keiciam = "".join(leet.get(c,c) for c in a.lower())

#print(keiciam)


def leet(tekstas):

    leets = {'a':'4','e':'3','i':'1','o':'0','A':'4','E':'3','I':'1','O':'0','d':'|>','n':"|\|",'u':'|_|','s':'5'}
    
    keiciam = "".join(leets.get(c,c) for c in tekstas.lower())
    return keiciam

a = input("Tekstas?")
a = leet(a)
print(a)