# pylint: disable= missing-docstring
# Task Nr.1:

# Create a class which takes temperature measurements in Kelvins and add static methods to transform those to Celsius and Fahrenheit units. Use OOP abstraction.
from abc import ABC, abstractmethod


class TemperatureConverter(ABC):
    @abstractmethod
    def to_celsius_and_fahrenheit(self) -> str:
        pass


class Temperature(TemperatureConverter):
    def __init__(self, temperature_in_kelvin: float):
        self.temperature_in_kelvin = temperature_in_kelvin

    def to_celsius_and_fahrenheit(self) -> str:
        return f"To celsius: {round(Temperature.to_celsius(self.temperature_in_kelvin),2)} C, " \
        f"to fahrenheit: {round(Temperature.to_fahrenheit(self.temperature_in_kelvin),2)} F"

    @staticmethod
    def to_celsius(temperature_in_kelvin: float) -> float:
        return temperature_in_kelvin - 273.15

    @staticmethod
    def to_fahrenheit(temperature_in_kelvin: float) -> float:
        return (temperature_in_kelvin * 9 / 5) + 32


print(Temperature.to_celsius(temperature_in_kelvin=294.15))

print(Temperature.to_fahrenheit(temperature_in_kelvin=294.15))

temp = Temperature(temperature_in_kelvin=294.15)
print(temp.to_celsius_and_fahrenheit())
