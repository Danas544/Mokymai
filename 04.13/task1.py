# Task Nr.1:

# Create a class called Product that takes a name and price as parameters and has __str__ and __repr__ methods defined.

# The __str__ method should return a string in the format "Product: name, Price: price"
# The __repr__ method should return a string in the format "Product('name', price)"


class Product():
    def __init__(self, name:str, price:float):
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'Product: {self.name}, Price: {self.price}'
    
    def __repr__(self) -> str:
        return f'Product({self.name}, {self.price})'
    

prod = Product(name='Pieva', price= 10.50)
print(prod)
print(repr(prod))