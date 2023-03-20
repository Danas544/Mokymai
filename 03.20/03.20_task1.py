# Task Nr.1:

# Create an abstract class Animal with which takes name of animal as an input and initialize it.
# The create speak abstract method, to be overridden by subclasses. And get_name method which returns name of the animal.

# Now create two subclasses of Animals: Dog and Cat which overrides the speak method,
# and provide the implementation which returns a string "Dog says Woof!" and "Cat says Meow!" respectively.


# from abc import ABC, abstractmethod


# class Animal(ABC):
#     def __init__(self, name: str) -> None:
#         self.name = name

#     @abstractmethod
#     def animal_speak(self) -> str:
#         pass

#     def get_name(self) -> str:
#         return self.name


# class Dog(Animal):
#     def __init__(self, name: str) -> None:
#         super().__init__(name=name)

#     def animal_speak(self) -> str:
#         return "Dog says Woof!"


# class Cat(Animal):
#     def __init__(self, name: str) -> None:
#         super().__init__(name=name)

#     def animal_speak(self) -> str:
#         return "Cat says Meow!"


# anim = Cat("Kate")
# anim2 = Dog("šuo")

# print(anim.get_name())
# print(anim.animal_speak())
# print(anim2.get_name())
# print(anim2.animal_speak())



class Animal():
    def __init__(self, name: str) -> None:
        self.name = name


    def animal_speak(self) -> str:
        raise NotADirectoryError

    def get_name(self) -> str:
        return self.name


class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def animal_speak(self) -> str:
        return "Dog says Woof!"


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name=name)

    def animal_speak(self) -> str:
        return "Cat says Meow!"


anim = Cat("Kate")
anim2 = Dog("šuo")

print(anim.get_name())
print(anim.animal_speak())
print(anim2.get_name())
print(anim2.animal_speak())


# class Animal():
#     def __init__(self, name: str) -> None:
#         self.name = name


#     def animal_speak(self) -> str:
#         pass

#     def get_name(self) -> str:
#         return self.name


# class Dog(Animal):
#     def __init__(self, name: str) -> None:
#         super().__init__(name=name)

#     def animal_speak(self) -> str:
#         return "Dog says Woof!"


# class Cat(Animal):
#     def __init__(self, name: str) -> None:
#         super().__init__(name=name)

#     def animal_speak(self) -> str:
#         return "Cat says Meow!"


# anim = Cat("Kate2")
# anim2 = Dog("šuo2")

# print(anim.get_name())
# print(anim.animal_speak())
# print(anim2.get_name())
# print(anim2.animal_speak())
