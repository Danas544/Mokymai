# https://github.com/CodeAcademy-Online/python-new-material-level2/wiki/1.-Clean-Code


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def say_hello(self) -> None:
        print(f"Hello, {self.name}")


Person_one = Person("first", "person")
Person_one.say_hello()


def greeting(full_name: str) -> None:
    """Function greets a person given full name as a string"""

    print(f"Hello {full_name.split()[0]} {full_name.split()[1]}, How are you today?")

def greet_user(age: int) -> None:
    eligiebleto_enter = age > 21

    if eligiebleto_enter == True:
        print("Welcome")
    if eligiebleto_enter == False:
        print("Access denied")
