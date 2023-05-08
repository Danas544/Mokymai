# You have been asked to create a simple inventory management system
# for a small retail store. You need to define a Product class using the dataclass module that represents
#  a product in the store. Each Product should have a unique ID, a name, a description, a price, and a quantity in  stock.
# You also need to implement a method calculate_total_cost that calculates the total cost of a given number of items of the product,
# taking into account any discounts that may apply.

from dataclasses import dataclass
from typing import Optional
@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float
    quantity: int

    def calculate_total_cost(self, number_of_items: Optional[int] = None) -> float:
        if number_of_items is None:
            return self.price * self.quantity
        else:
            return self.price * number_of_items


product1 = Product(id=1, name="Morka", description="Plautos", price=2.00, quantity=10)

print(product1.calculate_total_cost(number_of_items=20))
print(product1.calculate_total_cost())