# Task Nr.1:

# Create a class method to return the factorial of a given number.

import math

class Factorial:

    @classmethod
    def get_factorial(cls, number):
        return math.factorial(number)
    

print(Factorial.get_factorial(5))