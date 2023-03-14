class Names:
    """This is a class about our forgotten friend Antanas"""    
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name        
        self._surnname = surname        
        self.__age = age    
        def print_out_the_name(self) -> None:
            print(self.name)
    def change_name(self, name: str) -> None:
        print(self.__age)
        self.name = name# my_name = Names(name='Antanas', surname='Mindukas', age= 22)# my_name.change_name(name='Minde')# print(my_name.name)# print(my_name._surnname)# print(my_name.__age)# my_name.name = 'Minde'# print(my_name.name)# class Car:#     def __init__(self, make_year: int, cost: float, color: str) -> None:#         self.make_year = make_year#         self.cost = cost#         self.color = color#         self.full_info = f'Full info: {cost} linero - {make_year} years - {color}..'#         self.smth = None#     def get_car_color(self) -> None:#         print(f'My car color: {self.color}')#     def get_cost(self) -> float:#         return self.cost#     def get_full_info(self) -> None:#         print(f'My full info: {self.full_info}')class Car:
    def __init__(self, random_number: int) -> None:
        self._check_this_one: int = random_number        
        self.__check_another_one: int = 2    
        def get_car_color(self, color: str) -> None:
            print(f'My car color: {color}')
    def get_cost(self, cost: float) -> float:
        print(cost)
        return cost    
    def get_full_info(self, full_info: str) -> None:
        print(f'My full info: {full_info}')
class Plane:
    pass
class Ferrari(Car, Plane):
    SPEED_CONSTANT = 20.5    
    def __init__(self, hp: int, number: int) -> None:
        super().__init__(random_number=number)
        self.hp = hp    
        def _get_max_speed(self) -> float:
            return self.hp * self.SPEED_CONSTANT    
    def get_cost(self, cost: float) -> None:
        print(f'Cool Not COOl: {cost}')
    def calculate_consumption(self, distance: int) -> None:
        speed = self._get_max_speed()
        print(speed * distance)
test_car = Car(random_number=32550)
my_uber_car = Ferrari(hp= 450, number=555)
my_uber_car._get_max_speed()
print(test_car._check_this_one)
print(my_uber_car._check_this_one)
# print(my_uber_car.__check_another_one)# print(my_uber_car.__check_another_one)class My_Byke(Ferrari):
