from unit import Unit

class Sentinel(Unit): # Abstract

    def __init__(self, health, attack, armor, name, level, coords):
        super.__init__(health, attack, armor, name, level, coords)

    def type(self):
        return "sentinel"