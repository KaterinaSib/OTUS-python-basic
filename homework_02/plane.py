"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        if self.max_cargo >= self.cargo + add_cargo:
            self.cargo += add_cargo
        else:
            raise CargoOverload("Cargo exceeds maximum value")

    def remove_all_cargo(self):
        reset_cargo = self.cargo
        self.cargo = 0
        return reset_cargo
