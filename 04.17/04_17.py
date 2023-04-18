# my_list = ["Danielius", "Antanas"]


# for x in my_list:
#     yield x
#     print(x)


import time
def infinit():
    num = 0
    while True:
        num += 1
        yield num
        time.sleep(0.5)
        return "tekstas"


my_generator = infinit()
print(my_generator)



print(next(my_generator))

print(my_generator)

# print(next(my_generator))


# import sys

# x = [num**2 for num in range(10000)]
# y = (num**2 for num in range(10000))

# print(sys.getsizeof(x))
# print(sys.getsizeof(y))
