class Unit(object): # Abstract

    def __init__(self, health, attack, armor, name, level, coords):
        self._health = health
        self._attack = attack
        self._armor = armor
        self._name = name
        self._level = level
        self._coords = coords

    def type(self): # Abstract
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
    
