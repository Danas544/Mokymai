# Create an abstract class Money which takes currency and value as input and initializes it. A class must have these methods:

# get_value method which returns the value of the money.
# get_currency method which returns the currency of the money.
# convert_to_currency abstract method, which takes target currency and conversion rate as input and converts the value of the money to the target currency.

# Now create two subclasses of Money: Cash and Card. The Cash class should take the denomination of the cash as input in the constructor, and should implement the convert_to_currency method.
#  The Card class should take the credit limit of the card as input in the constructor, and should implement the convert_to_currency method using the conversion rate to convert the value of the
#   card to the target currency.
from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, currency: str, value: float) -> None:
        self.currency = currency
        self.value = value

    def get_value(self) -> float:
        return self.value

    def get_currency(self) -> str:
        return self.currency

    @abstractmethod
    def convert_to_currency(self) -> str:
        pass


class Card(Money):
    def __init__(self, currency: str, value: float, credit_limit: int) -> None:
        self.credit_limit = credit_limit
        super().__init__(currency=currency, value=value)

    def get_credit_limit(self) -> int:
        return self.credit_limit

    def convert_to_currency(self) -> str:
        return f"from {self.currency} convert to £ amount: {self.value * 0.87}£"


class Cash(Money):
    def __init__(self, currency: str, value: float, denomination: int) -> None:
        self.denomination = denomination
        super().__init__(currency, value)

    def get_denomination(self) -> int:
        return self.denomination

    def convert_to_currency(self) -> str:
        return f"from {self.currency} convert to £ amount: {self.value * 0.87}£"


kreditine = Card(currency="EUR", value=10000.51, credit_limit=111111)
print(kreditine.get_currency())
print(kreditine.get_value())
print(kreditine.convert_to_currency())
print(kreditine.get_credit_limit())


print("\n")
gryni_pinigai = Cash(currency="EUR", value=50000.51, denomination=500)
print(gryni_pinigai.get_currency())
print(gryni_pinigai.get_value())
print(gryni_pinigai.convert_to_currency())
print(gryni_pinigai.get_denomination())
