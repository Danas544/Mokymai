import datetime

class Person:
    def __init__(self , name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def greet(self):
        return f"Hello my name is {self.name}"
    
    def calculate_days_left_till_back_friday(self) -> int:
        dabartine = datetime.date.today()
        black_friday_data = datetime.date(2023,11,24)
        skirtumas = black_friday_data - dabartine
        return skirtumas.days


    def get_eye_color(self, eye_color: str ="Green") -> str:
        return eye_color
    
    def __str__(self) -> str:
        return f"P :  {self.name}--{self.surname}"

    def __repr__(self) -> str:
        return f"Person: {self.name}--{self.surname}"
    






person = Person("Danielius" , "Au")
print(person)
# print(person.get_eye_color("Blue"))
# print(person.calculate_days_left_till_back_friday())



person2 = Person("Antanas" , "Au_Antanas")


# print(person.name)
# print(person2.name)
# print(person.greet())
# print(person2.greet())

