# Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.

# Example:

# For input: [3, 4, 4, 3, 6, 3]

# remove the 3 at index 0
# remove the 4 at index 1
# remove the 3 at index 3

# Expected output: [4, 6, 3]

# More examples can be found in the test cases.

# Good luck!

def solve(arr): 
    new = []
    for i in arr[::-1]:
        if i not in new:
            new.append(i)
        else:
            del new[new.index(i)]
            new.append(i)
    return new[::-1]

    
    
print(solve([3,4,4,3,6,3]))