"""Module contains superheroes classes."""
from weapon_classes import Gunslinger, Karateka


class SuperHero:
    """Basic superhero class."""

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack

    @staticmethod
    def find(place):
        """Find antagonists to fight based on location."""
        place.get_antagonist()

    def attack(self):
        """Use common attacks or something special."""
        try:
            self.fire_a_gun()
        except AttributeError:
            try:
                self.roundhouse_kick()
            except AttributeError:
                print('Is it a bird? Is it a plane?')

    def ultimate(self):
        """Ultimate attack, different for every hero."""
        pass


class Superman(SuperHero):
    """The last son of a dying world with eye-lasers as ultimate weapon."""
    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def ultimate(self):
        """Superman's ultimate attack."""
        print('Wzzzuuuup!')


class BlackWidow(SuperHero, Gunslinger):
    """A former Russian spy with expert gunfire skills."""
    def __init__(self):
        super(BlackWidow, self).__init__('Natasha Romanoff', False)


class Shaun(SuperHero, Karateka):
    """A martial artist superhero, dispels stereotypes."""

    def __init__(self):
        super(Shaun, self).__init__('Shang-Chi', False)
