# pylint: disable=all# mypy: ignore-errors# flake8: noqafrom dataclasses import dataclassfrom typing import List# class Position:#     def __init__(self, name: str, lan: float, long: float) -> None:#         self.name = name#         self.lan = lan#         self.long = long@dataclassclass Position:
    name: str    lan: float    long: floatclass LithuanianCities:
    VILNIUS = Position(name="VILNIUS", long=0.2, lan=0.3)
    KAUNAS = Position(name="KAUNAS", long=0.2, lan=0.3)
pos = Position(name="Vilnius", lan=0.01, long=0.01)
print(pos.name, pos.lan, pos.long)
@dataclassclass Guest:
    name: str    bill: float    position: Position    def get_bill(self) -> float:
        return self.bill    def get_guest_location(self) -> str:
        return self.position.name# class Guest:#     def __init__(self, name: str, bill: float, position: Position) -> None:#         self.name = name#         self.bill = bill#         self.position = position#     def get_bill(self) -> float:#         return self.bill#     def get_guest_location(self) -> str:#         return self.position.namefirst_guest = Guest(name="AA", bill=0.01, position=LithuanianCities.VILNIUS)
print(first_guest.get_bill())
print(first_guest.position.name)