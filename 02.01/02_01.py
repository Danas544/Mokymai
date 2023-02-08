
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 
# (every 6 will be followed by at least one 7). Return 0 for no numbers.


def sum67(nums):  
    for x in nums:
        if x >= 6:
            pass          
        else:
            tuscias.append(x)
    suma = sum(tuscias)
    return suma


list=[1,1,1,1,6,10]
tuscias = []

print(sum67(list))

