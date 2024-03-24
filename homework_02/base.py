from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        while not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Fuel is not enough to start')

    def move(self, distance):
        if self.fuel >= self.fuel_consumption * distance:
            self.fuel -= (self.fuel_consumption * distance)
        else:
            raise NotEnoughFuel('Fuel is not enough')

