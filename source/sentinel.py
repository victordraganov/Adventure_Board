from unit import Unit


class Sentinel(Unit):  # Abstract

    def __init__(self, name, health, attack, armor,  level, coords, speed):
        Unit.__init__(self, name, health, attack, armor, level, coords, speed)

    def type(self):
        return "sentinel"

# from coords import Coords
# coords = Coords(4,4)
# sent = Sentinel("doge", 4,4,4,4,coords,5)
