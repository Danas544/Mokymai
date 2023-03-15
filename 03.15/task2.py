# Task Nr.2:

# Create a Bus, Taxi, Train child classes that inherits from the Vehicle class.
# Implement at least five methods in a superclass what would describe those vehicles.
# The default fare charge of any vehicle is seating capacity * 100 . If Vehicle is Bus
# instance, we need to add an extra 10% on full fare as a maintenance charge.


class Vehicle:
    def __init__(
        self, color: str, model: str, places: int, brands: str, make_year: int
    ) -> None:
        self.color = color
        self.model = model
        self.places = places
        self.brands = brands
        self.make_year = make_year

    def get_color(self):
        return self.color

    def get_model(self):
        return self.model

    def get_places(self):
        return self.places

    def get_brand(self):
        return self.brands

    def get_make_year(self):
        return self.make_year


class Bus(Vehicle):
    def __init__(
        self, color: str, model: str, places: int, brands: str, make_year: int
    ) -> None:
        self.places = places
        super().__init__(color, model, places, brands, make_year)


    def ticket_price(self) -> float:
        return (self.places * 100) * 10 / 100 + (self.places * 100)


class Taxi(Vehicle):
    def __init__(
        self,
        color: str,
        model: str,
        places: int,
        brands: str,
        make_year: int,
        travel_distance: int,
    ) -> None:
        super().__init__(color, model, places, brands, make_year)
        self.travel_distance = travel_distance

    def ticket_price(self) -> float:
        return (0.80 * self.travel_distance) * 10 / 100 + (0.80 * self.travel_distance)


class Train(Vehicle):
    def __init__(
        self, color: str, model: str, places: int, brands: str, make_year: int
    ) -> None:
        self.places = places
        super().__init__(color, model, places, brands, make_year)


    def ticket_price(self) -> float:
        return (self.places * 50) * 10 / 100 + (self.places * 50)


traukinys = Train(
    color="melyna", model="TR100", places=112, brands="Traukinio firma", make_year=2023
)
print(traukinys.ticket_price())
print(f'Metai: {traukinys.get_make_year()} , spalva: {traukinys.get_color()}, modelis: {traukinys.get_model()}, marke: {traukinys.get_brand()}')


buss = Bus(color="raudonas", model="V100", places=50, brands="Volvo", make_year=2023)
print(buss.ticket_price())
print(f'Metai: {buss.get_make_year()} , spalva: {buss.get_color()}, modelis: {buss.get_model()}, marke: {buss.get_brand()}')


taksi = Taxi(
    color="zalias",
    model="Prius",
    places=4,
    brands="Toyota",
    make_year=2023,
    travel_distance=10,
)
print(taksi.ticket_price())
print(f'Metai: {taksi.get_make_year()} , spalva: {taksi.get_color()}, modelis: {taksi.get_model()}, marke: {taksi.get_brand()}')
