# Create a Person class which will have three properties:
#     Name
#     List of foods they like
#     List of foods they hate
# In this class, create the method taste():
#     It will take in a food name as a string.
#     Return {person_name} eats the {food_name}.
#     If the food is in the person's like list, add 'and loves it!' to the end.
#     If it is in the person's hate list, add 'and hates it!' to the end.
#     If it is in neither list, simply add an exclamation mark to the end.
#     p1 = Person("Sam", ["ice cream"], ["carrots"])
#     p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
#     p1.taste("cheese") ➞ "Sam eats the cheese!"
#     p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"


class Person:
    def __init__(self, name: str, food_like: list[str], food_hate:list[str]) -> None:
        self.name = name
        self.food_like = food_like
        self.food_hate = food_hate



    def taste(self, food: str)-> str:
        if food not in self.food_hate and food not in self.food_like:
            return f"{self.name} eats the {food}!"
        elif food in self.food_hate:
            return f"{self.name} eats the {food} and hates it!"
        else:
            return f"{self.name} eats the {food} and loves it!"


p1 = Person(name= "Danielius", food_like= ["Agurkas", "Ledai", "Kebabas"], food_hate= ["Pomidorai", "ryžiai","Kiaule"])

print(p1.taste('ryžiai'))