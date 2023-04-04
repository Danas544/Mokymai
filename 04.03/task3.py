# Task Nr.3:

# Create a class method to return the list of prime numbers up to a given number.
from typing import List

class MathOperations:
    @classmethod
    def is_prime(cls, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @classmethod
    def primes(cls, n: int) -> List[int]:
        primes_list = []
        for i in range(2, n+1):
            if cls.is_prime(i):
                primes_list.append(i)
        return primes_list

print(MathOperations.primes(20)) 