# Task Nr.1:
# Write a Temperature class that has a celsius property and a fahrenheit property.
#  The celsius property stores the temperature in Celsius, and the fahrenheit property stores the temperature in Fahrenheit.
#  The fahrenheit property should be a computed property that converts the Celsius temperature to Fahrenheit.


class Temperature(object):
    def __init__(self, temperature: float):
        self._temperature = temperature
    

    @property
    def celsius(self)  -> float:
        return self._temperature


    @celsius.setter
    def celsius(self, value: float) -> None:
        self._temperature = value

    @property
    def fahrenheit(self) -> str:
        return f'{ (self._temperature * 1.8) + 32} fahrenheit'
    

temp = Temperature(temperature=20.50)
print(temp.celsius)
print(temp.fahrenheit)
temp.celsius = 50.5
print(temp.fahrenheit)