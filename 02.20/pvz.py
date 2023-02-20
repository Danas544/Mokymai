# def fourth_func(name: str = "Laimonas") ->None:
#     try:
#         name[-4] == "Y"        
#         print(name)
#     except Exception as e:
#         print(f"Exception {e}")
# fourth_func(name="H")

def fifth_func(name: str, surname: str) -> None:
    try: 
        full_name = name + surname       
        print(Hello, world)
    except Exception as e:
        print(f"That was scary error - {e}")
    else:
        print(full_name)
fifth_func(name = "Laimonas", surname= "Paura")



# def third_func(number: int) -> None:
#     try:
#         number = 20 / number        
#         print(number)
#     except ZeroDivisionError:
#         print("do not divide by zero")
# third_func(number=0)
