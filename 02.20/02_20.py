from typing import Union

def div(number: Union[float,int]) -> Union[float,int]:
    try:
        return number / 2 if isinstance(number,float) else number // 2
    except TypeError:
        print("Error")
    except Exception as e:
        print(f"Error: {e}")
    # finally:
    #     print("OK OK OK")

# try:
#     a = div("10")
#     print(a) 
#     print(a / 0)

# except TypeError:
#     print("Blogai")
# except ZeroDivisionError:
#     print("Negali buti 0")



try:
    my_div = div(10)
    print(my_div)
    print(my_div / 5)
except ZeroDivisionError:
    print("alo")
except Exception as e:
    print(f"Error: {e}")
else:
    print("ok")
finally:
    print("OK OK OK")




