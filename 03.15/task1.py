# class Shape:
#     def __init__(self, name: str, sides: int) -> None:
#         self.name = name
#         self.sides = sides

#     def area(self) -> float:
#         raise NotImplementedError

# class Rectangle(Shape):
#     def __init__(self, width: float, height: float) -> None:
#         super().__init__("Rectangle", 4)
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return self.width * self.height

# class Square(Rectangle):
#     def __init__(self, side_length: float) -> None:
#         super().__init__(side_length, side_length)
#         self.side_length = side_length

# square = Square(6)
# print(square.name)  # prints "Rectangle"
# print(square.sides)  # prints 4
# print(square.area())  # prints 25


class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name = name
        self.sides = sides


class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        super().__init__(name="Stačiakampis", sides="4")

    def area(self) -> int:
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length: int) -> None:
        self.side_length = side_length
        super().__init__(width=side_length, height=side_length)


kvadratas = Square(side_length=6)
print(kvadratas.name)
print(kvadratas.area())
print(kvadratas.sides)
