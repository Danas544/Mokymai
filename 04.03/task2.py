# Task Nr.2:

# Create a class method to return the reversed string of a given string.


class ReverseString:
    @classmethod
    def reverse_string(cls, string: str) -> str:
        return string[::-1]


print(ReverseString.reverse_string("Danielius"))
