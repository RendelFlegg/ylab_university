"""Module contains mixins for creating superheroes."""


class Gunslinger:
    """Mixin for a hero with the gun."""
    @staticmethod
    def fire_a_gun():
        print('PIU PIU')


class Karateka:
    """Mixin for a hero with martial arts skills."""
    @staticmethod
    def roundhouse_kick():
        print('Bump')
