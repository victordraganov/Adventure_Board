from hero import Hero
from coords import Coords

INITIAL_MONEY = 500  # Starting amount of money. (NOT FOR GOOD)


class Player(object):

    """
        Player represents one acting player in the game.
        Player((player_name, hero_name), Hero)
    """

    def __init__(self, name, hero):
        self._name = name
        self._hero = hero
        self._money = INITIAL_MONEY

    @property
    def name(self):
        return self._name

    @property
    def coords(self):
        return self._hero.coords

    @property
    def money(self):
        return self._money

    @property
    def player_luck(self):
        return self._hero.luck
    

#coords = Coords(4, 4)
#hero = Hero('gosho', 5, 5, 5, 5,  coords, 'assassin', 5)
#player = Player('conko', hero)
