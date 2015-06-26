from board_object import BoardObject

INITIAL_LUCK = 4  # MIN 0 MAX 10
UNIT_SIZE = (1, 1)  # THE INITIAL UNIT SIZE -> 1 FIELD


class Unit(BoardObject):  # Abstract

    def __init__(self, name, level, coords, speed, luck, strength,
                 agillity, wisdom, attack_type):
        BoardObject.__init__(self, name, level, coords, UNIT_SIZE)
        self._strength = strength
        self._agillity = agillity
        self._wisdom = wisdom
        self._attack_type = attack_type
        self._level = level
        self._speed = speed
        self._luck = luck

    @property
    def attack_type(self):
        return self._attack_type

    @property
    def speed(self):
        return self._speed

    @property
    def luck(self):
        return self._luck

    def type(self):  # Abstract
        pass

    def init_characteristics(self):  # Abstract
        pass


# from coords import Coords
# coords = Coords(4, 400)
# unit = Unit('dog', 4, 4, 4, 4, coords, 5)
# print(unit.level)
