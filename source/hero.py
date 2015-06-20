from unit import Unit


class Hero(Unit):

    def __init__(self, name, health, damage, armor, level,
                    coords, speed, luck, hero_category):
        Unit.__init__(self, name, health, damage, armor,
                        level, coords, speed, luck)
        self._energy = 100
        self._hero_category = hero_category
        self.init_attack_type()
        self._experience = 0
        self._skills = []
        # inventory

    @property
    def hero_category(self):
        return self._hero_category

    @property
    def experience(self):
        return self._experience

    @property
    def energy(self):
        return self._energy

    @property
    def skills(self):
        return self._skills
    
    
    def type(self):
        return "hero"

    # Initializes the hero as a "hitter" or "shooter"
    def init_attack_type(self):
        if self.hero_category == "assassin" or self.hero_category == "warior":
            self._attack_type = "melee"
        else:
            self._attack_type = "range"

    def gain_exp(self, amount):
        self._experience = self.experience + amount

    def learn_skill(self, new_skill):
        self._skills.append(new_skill)

    def level_up(self):
        self._level = self._level + 1

# from coords import Coords
# coords = Coords(4, 4)
# hero = Hero('shoho', 5, 5, 5, 5, coords, 'assassiin')
# hero.gain_exp(50)
# print(hero.experience)
