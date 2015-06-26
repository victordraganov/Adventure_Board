from unit import Unit


class Sentinel(Unit):  # Abstract

    def __init__(self, name, level, coords, speed, luck, strength,
                 agillity, wisdom, attack_type):
        Unit.__init__(self, name, level, coords, speed, luck, strength,
                      agillity, wisdom, attack_type)

    def init_characteristics(self):
        self._damage =
        self._armor

    def type(self):
        return "sentinel"

# from coords import Coords
# coords = Coords(4,4)
# sent = Sentinel("doge", 4,4,4,4,coords,5)
