class Person:
    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.age = age
    
    def get_name(self)-> str:
        return self.__name




me = Person(name= "Danielius", age= 20)

print(me.age)
print(me.get_name())