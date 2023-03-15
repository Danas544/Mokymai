class Vehicle:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def get_name(self) -> str:
        """get name"""
        return self.name


class Engine:
    def __init__(self, name: str) -> None:
        self.name = name

    def say_hi_engine(self) -> None:
        """Hello engine"""
        print(f"hi engine with name {self.name}")


class Golfiukas(Vehicle, Engine):
    def __init__(self, name: str, cost: float) -> None:
        super().__init__(name=name)
        Engine.__init__(self, name=name)
        self.cost: float = cost

    def get_cost(self) -> float:
        """return cost"""
        return self.cost
