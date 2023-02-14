# def find_sum( num1 , num2 ):
#     sum_nums = num1 + num2 # Suranda num1 ir num2 sumą
#     return sum_nums # Grąžina skaičių sumą



# num1 , num2 = input("tsk skaiciai:" )

# print(find_sum(int(num1) ,int(num2)))


# def even_odd(num):

#     '''
#     Grąžina "lyginis", jei num yra lyginis, ir "nelyginis", jei num yra nelyginis.    
#     Parametrai:
#         (int): Grąžinama:
#         type (eilutė): "lyginis", jei num yra lyginis; "nelyginis", jei num yra nelyginis
#     '''

#     if num % 2 == 0: # Patikrina, ar num/2 turi likutį 0
#         return f"lyginis {num}" # Jei likutis lygus 0, grąžinama "lyginis"
#     else:
#        return f"ne lyginis {num}" # Jei neturi, grąžinama "nelyginis".


# print(even_odd(3))


# def check_if_exist(a=None):
#   if a:
#     return a
#   return

# a = check_if_exist("b")
# print(a)

# def add_two_int_numbers(a: int,b: int)-> int:
#     return a + b


# a = add_two_int_numbers(10, 5)
# print(type(a))


# type_annotation_int: int = 43
# type_annotation_float: float = 2.54
# type_annotation_string: str = 'efe'
# type_annotation_bool: bool = True



# def check_arguments(mandatory, *args, **kwargs) -> None:
#     print (mandatory)
#     if args:
#         print (args)
#     if kwargs:
#         print (kwargs)

# check_arguments(1 , 5, 6)

# check_arguments('welcome')
# check_arguments('welcome', 1, 2, 3)
# check_arguments('welcome', 1, 2, 3, name='Sarah', age=26)



# multiplication= lambda x,y : x * y
# print(multiplication(2,3))
pirmas = [1, 2, 3, 4]
antras = [4, 5, 2, 1]


#print(a)
def puzzle(pirmas_listas , antras_listas):
    bendras = []
    for pirm, antr in zip(pirmas, antras):
        sudetis = pirm + antr
        bendras.append(sudetis)
    tikrinam = bendras[0]
    for x in bendras:
        if x == tikrinam:
            pass
        else:
            return False
    return True



print(puzzle(pirmas,antras))

