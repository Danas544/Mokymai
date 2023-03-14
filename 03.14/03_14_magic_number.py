# Task Nr.2: Magic Number problem. A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by
#  adding the sum of the digits after every addition. If the single digit comes out to be 1,then the number is a magic number.
# For example Number = 50113 => 5+0+1+1+3=10 => 1+0=1 This is a Magic Number

# For example Number = 1234 => 1+2+3+4=10 => 1+0=1 This is a Magic Number

# Write a python function that takes in one parameter - integer and then returns True if number is magic number or False if it is not a magic number


def magic_number(numbers: int) -> bool:
    string = str(numbers)
    numbers_list = []
    for number in string:
        numbers_list.append(int(number))

    sum_number = sum(numbers_list)
    sum_number_list = []

    for number in str(sum_number):
        sum_number_list.append(int(number))

    if sum(sum_number_list) == 1:
        return True
    else:
        return False


print(magic_number(50113))


def is_magic_number(number: int) -> bool:
    number = str(number)
    if len(number) == 1:
        if number == "1":
            return True
        else:
            return False
    else:
        number = sum([int(n) for n in number])
        return is_magic_number(number)


print(is_magic_number(50113))
