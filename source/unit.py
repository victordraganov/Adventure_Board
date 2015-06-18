INITIAL_LUCK = 4  # MIN 0 MAX 10


class Unit:  # Abstract

    def __init__(self, name, health, damage, armor,  level, coords, speed):
        self._name = name
        self._health = health
        self._damage = damage
        self._armor = armor
        self._level = level
        self._coords = coords
        self._speed = speed
        self._luck = INITIAL_LUCK

    def type(self):  # Abstract
        pass

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def coords(self):
        return self._coords

    @property
    def speed(self):
        return self._speed

    @property
    def luck(self):
        return self._luck


# from coords import Coords
# coords = Coords(4, 400)
# unit = Unit('dog', 4, 4, 4, 4, coords, 5)
# print(unit.level)
