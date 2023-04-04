# Task Nr.1:
# Nasa needs to calculate expenses for the new mission: using OOP principles implement Base and Space Shuttle classes. Create a simple calculator with:
# Base class should give a functionality to know info about spacecraft (age, cost, year built, weight etc.. ).
# Through the main class you should be able to calculate the mission cost which includes: fuel cost
# (FUEL_COST x BURN_RATE (kg/mile) * BURN_RATE_VARIABLE (2500 / orbit_height(in miles))) , average personals expenditures ( ppl x base_salary ).
# Prepare the final report in the file document and on screen with a method get_full_report with all gathered and calculated data.

# NASA turi apskaičiuoti išlaidas naujai misijai: pagal OOP principus įgyvendina Base ir Space Shuttle klases. Sukurkite paprastą skaičiuotuvą naudodami:
#   Bazinė klasė turėtų suteikti galimybę žinoti informaciją apie erdvėlaivį (amžių, kainą, pagaminimo metus, svorį ir pan.).
#   Per pagrindinę klasę turėtumėte mokėti apskaičiuoti komandiruotės išlaidas, į kurias įeina: degalų sąnaudos
#   (FUEL_COST x BURN_RATE (kg/myl.) * BURN_RATE_VARIABLE (2500 / orbitos_aukštis (myliomis)))) , vidutinės asmeninės išlaidos (žmogus x bazinis atlyginimas).
#   Paruoškite galutinę ataskaitą failo dokumente ir ekrane naudodami metodą get_full_report su visais surinktais ir apskaičiuotais duomenimis.
import datetime
import logging
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    filename="report.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


class Carrier:
    """Shuttle cost currency is EUR
    shuttle weight is in kg
    year built format YYYY"""

    def __init__(self, cost: float, year_built: int, weight: float) -> None:
        self._cost: float = cost
        self._year_built: int = year_built
        self._weight: float = weight

    def get_cost(self) -> float:
        return self._cost

    def get_year_built(self) -> int:
        return self._year_built

    def get_weight(self) -> float:
        return self._weight

    def get_age(self) -> int:
        return datetime.date.today().year - self._year_built


# fuel cost
# (FUEL_COST x BURN_RATE (kg/mile) * BURN_RATE_VARIABLE (2500 / orbit_height(in miles))) , average personals expenditures ( ppl x base_salary ).


class SpaceShuttle(Carrier):
    """orbit_height in miles"""

    LEMPA = 2500

    def __init__(self, cost: float, year_built: int, weight: float) -> None:
        super().__init__(cost=cost, year_built=year_built, weight=weight)
        self.fual_cost = None
        self.average_personals_expenditures = None
        self.mission_cost = None

    def _get_burn_rate_variable(self, orbit_height: float) -> float:
        return self.LEMPA / orbit_height

    def get_fuel_cost(self, fuel_cost: float, burn_rate: float, orbit_height: float):
        burn_rate_variable = self._get_burn_rate_variable(orbit_height=orbit_height)
        self.fual_cost = (fuel_cost * burn_rate) * burn_rate_variable
        return self.fual_cost

    def get_average_personals_expenditures(
        self, peaple_count: int, base_salary: float
    ) -> float:
        self.average_personals_expenditures = peaple_count * base_salary
        return self.average_personals_expenditures

    def get_mission_cost(
        self,
        fuel_cost: float,
        burn_rate: float,
        orbit_height: float,
        base_salary: float,
        peaple_count: int,
    ):
        expedition_fuel_cost = self.get_fuel_cost(
            fuel_cost=fuel_cost, burn_rate=burn_rate, orbit_height=orbit_height
        )
        average_personal_cost = self.get_average_personals_expenditures(
            peaple_count=peaple_count, base_salary=base_salary
        )
        self.mission_cost = expedition_fuel_cost + average_personal_cost
        return self.mission_cost

    def get_full_report(self)-> dict[str,Union[None,int]]:
        full_report = {
            "Cost": self.get_cost(),
            "Year_built": self.get_year_built(),
            "Weight": self.get_weight(),
            "Age": self.get_age(),
            "Fuel_cost": self.fual_cost,
            "Average_personals_expenditures": self.average_personals_expenditures,
            "Mission_cost": self.mission_cost,
        }
        logging.info(full_report)
        return full_report


space = SpaceShuttle(50000, 6000, 800)

space.get_mission_cost(
    fuel_cost=6000,
    burn_rate=21.00,
    orbit_height=1000000,
    peaple_count=1000,
    base_salary=2000,
)
full_report = space.get_full_report()
