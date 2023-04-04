# pylint: disable= missing-docstring


class Circle:
    def __init__(self):
        self.name = "Circle"

    def print_my_name(self):
        print(self.name)

    @staticmethod
    def print_another_name(name: str):
        print(f"name: %s" % name)


print(Circle.print_another_name("Danielius"))
