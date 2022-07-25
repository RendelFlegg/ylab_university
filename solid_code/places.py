"""Module with location classes."""
from abc import ABC, abstractmethod


class Place(ABC):
    """Parent class for all locations."""
    @abstractmethod
    def get_antagonist(self):
        pass


class Kostroma(Place):
    """The Kostroma location with orcs as antagonists."""
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    """The Tokyo location with Godzilla as antagonist."""
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Hala(Place):
    """The Hala planet with coordinates instead of name and scrulls as antagonists."""
    coordinates = [0.15, 3.17]

    def get_antagonist(self):
        print('Skrulls have arrived')
