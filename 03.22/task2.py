# write a function that accepts a number as a parameter. The function should return a number that’s the difference between
# the largest and smallest numbers that the digits can form in the number.For example,
# if the parameter is “213”, the function should return “198”, which is the result of 123 subtracted from 321.


def difference(number: str) -> int:
    return int("".join(sorted(number, reverse=True))) - int("".join(sorted(number)))


print(difference("512"))
