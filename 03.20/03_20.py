# from abc import ABC, abstractmethod


# class Vehicle(ABC):
#     @abstractmethod
#     def get_names(self) -> None:
#         """to get vehicle name"""
#         pass

#     @abstractmethod
#     def get_vehicle_cost(self) -> None:
#         """get vehicle cost"""
#         pass


# class Car(Vehicle):
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

#     def get_age(self) -> None:
#         print(self.age)


#     def get_names(self) -> None:
#         """to get vehicle name"""
#         print(self.name)


#     def get_vehicle_cost(self) -> None:
#         """get vehicle cost"""
#         print("Too much anyways")
  

# my_car = Car(name="Volvo", age=2018)
# my_car.get_age()
# print(my_car.get_vehicle_cost())
# my_car.get_names()


class Vehicle:
    def get_smth(self):
        pass

    def do_smth(self):
        raise NotADirectoryError
    

class Combain(Vehicle):
    
    def do_smth(self):
         print('Doing smth')

my_veh = Combain()
print(my_veh.do_smth())



