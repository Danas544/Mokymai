# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x):
# You can use input to receive the number. Example:
# n= 5 , output:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


sk = int(input("skaicius: "))

dk = {}

i = 1
while sk >= i:
    dk[i] = i * i

    #print(dk)
    i += 1
print(dk)

dks = {}

for x in range(1, sk + 1):
    dks[x] = x * x
print(dks)