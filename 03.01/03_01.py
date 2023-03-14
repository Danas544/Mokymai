# class Names:

#     def __init__(self, name: str, surname: str, age: int) -> None:
#         self.name = name
#         self._surname = surname
#         self.__age = age


# my_name = Names(name="Danielius",surname="Au", age= 25)

# print(my_name.name)
# print(my_name._surname)
# my_name = Names(name="Antanas",surname="ANTANUKAS", age= 30)

# print(my_name.name)
# print(my_name._surname)


class Car:
    # def __init__(self, make_year:int, cost: float, color: str) -> None:
    #     self.make_year = make_year
    #     self.cost = cost
    #     self.color = color
    #     self.full_info = f'Kaina: {cost} Spalva: {color} Metai: {make_year}'
    def __init__(self) -> None:
        self._check_this_one = 1
        self.__check_another_one = 5

    def get_car_color(self, color):
        print(f"Masinos spalva {color}")

    def get_cost(self)-> float:
        return self.cost
    
    def get_full_info(self):
        print(f"{self.full_info}")


class Ferrari(Car):
    SPEED_CONTANT = 20.5
    def __init__(self, hp: int) -> None:
        super().__init__()
        self.hp = hp

    def get_max_speed(self)-> float:
        return self.hp * self.SPEED_CONTANT
    
uber_car = Ferrari(hp=450)
print(f'max speed: {uber_car.get_max_speed()}')

uber_car.get_car_color("white")
print(uber_car._check_this_one)
# print(uber_car.__check_another_one)

