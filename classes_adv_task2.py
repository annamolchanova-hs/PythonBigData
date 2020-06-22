from abc import ABC
from abc import abstractmethod


class Vehicle(ABC):
    def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    def vehicle_type(self) -> str:
        """ имя и тип транспортного средства (ТС)"""
        return f"{self.brand_name} {self.__class__.__name__}"

    @property
    @abstractmethod
    def wheels(self):
        return 4

    def is_motorcycle(self) -> bool:
        return self.wheels == 2

    def purchase_price(self) -> float:
        """
        выводит стоимость ТС в зависимости от кол-ва пройденных км: (базовая цена - 0.1 * кол-во км).
        Если получился меньше "100" - вернуть "100".
        """
        price = self.base_price - 0.1 * self.mileage
        return price if price > 100 else 100


class Car(Vehicle):
    wheels = 4


class Motorcycle(Vehicle):
    wheels = 2


class Truck(Vehicle):
    wheels = 4


class Bus(Vehicle):
    wheels = 4


vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000),
)

for vehicle in vehicles:
    print(
        f"Vehicle type={vehicle.vehicle_type()}\n"
        f"Is motorcycle={vehicle.is_motorcycle()}\n"
        f"Purchase price={vehicle.purchase_price()}\n"
    )
