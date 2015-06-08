from unit import Unit

class Hero(Unit):

    def __init__(self, health, attack, armor, name, level, coords, hero_type):
        super.__init__(health, attack, armor, name, level, coords)
        self._energy = 100
        self._hero_type = hero_type
        self._experience = 0

    @property
    def hero_type(self):
        return self._hero_type

    @property
    def experience(self):
        return self._experience
    
    def level_up(self):
        self._level = self._level + 1

    def gain_exp(self, amount):
        self._experience = self.experience + amount

    def type(self):
        return "hero"