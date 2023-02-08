a = ["Sveiki"]
b = ["visi"]


sudetis = a + b
print(sudetis)

c = [1 , 2]
g = [10, 20]
pirmas = []


for x,y in c,g:
    sudedam = x + y
    pirmas.append(sudedam)


print(pirmas)
print(sum(pirmas))


