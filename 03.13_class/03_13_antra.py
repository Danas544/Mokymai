# Create a class Smoothie and do the following:
#     Create an instance attribute called ingredients.
#     Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
#     Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
#     Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence.
#  If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
# Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call all methods you implemented.


class Smoothie:
    def __init__(self , patiekalai: dict) -> None:
        self.ingredients = patiekalai


    def get_name(self) -> str:
        ingred = []
        for name in self.ingredients["Patiekalai"]:
            ingred.append(name["name"])
        if len(ingred) > 1:
            return f'{" ".join(sorted(ingred))} Fusion'
        else:
            return f'{" ".join(sorted(ingred))} Smoothie'


    
    def get_cost(self) -> int:
        total_smoothie_price = []
        for kaina in self.ingredients["Patiekalai"]:
            total_smoothie_price.append(kaina["kaina"]["value"])
        return sum(total_smoothie_price)
        

    def get_price(self, total_smoothie_price: int) -> float:
        return round(total_smoothie_price * 1.5, 2)



class Alc_Smoothie(Smoothie):
    def __init__(self, patiekalai: dict) -> None:
        super().__init__(patiekalai)

class Non_alc_Smoothie(Smoothie):
    def __init__(self, patiekalai: dict) -> None:
        super().__init__(patiekalai)



alc_Kokteilis = Alc_Smoothie({
    "Patiekalai":[
    {
    "name": "viskis",
    "kaina":{
    "value":1
    }
    },{
    "name": "braskes",
    "kaina":{
    "value":2
    }
    }
    ]
})


non_alc_kokteilis = Non_alc_Smoothie({
    "Patiekalai":[
    {
    "name": "ledai",
    "kaina":{
    "value":5
    }
    },{
    "name": "bananai",
    "kaina":{
    "value":2
    }
    }
    ]
})



print(alc_Kokteilis.get_cost())
print(alc_Kokteilis.get_price(alc_Kokteilis.get_cost()))
print(alc_Kokteilis.get_name())


print(non_alc_kokteilis.get_cost())
print(non_alc_kokteilis.get_price(non_alc_kokteilis.get_cost()))
print(non_alc_kokteilis.get_name())