from hero import Hero

class Player(object):
    def __init__(self, name, hero):
        self._name = name
        self._hero = hero

    @property
    def money(self):
        return self._money
    