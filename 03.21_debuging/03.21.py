# write a python script that adds all the numbers entered
# in the command line as arguments. Throw an error if user enters something other than number

import sys

suma = []
try:
    for x in sys.argv[1:]:
        suma.append(int(x))
except Exception as e:
    print(f"Reikia skačiu: {e}")


print(sum(suma))
