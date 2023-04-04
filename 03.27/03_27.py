# Task Nr.1:

# Create a class Person that has two methods: set_name and set_age,
# which set the name and age attributes of the class, respectively. Modify these methods to return self, so that the calls can be chained together.


class Person:
    def __init__(self) -> None:
        self.name = None
        self.age = None

    def give_name(self, name: str) -> "Person":
        self.name = name
        return self

    def give_age(self, age: int) -> "Person":
        self.age = age
        return self

person_one = Person()

person_one.give_name("Danielius").give_age(25)

print(f"Mano vardas: {person_one.name}, metai: {person_one.age}")