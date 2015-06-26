from neutral import Neutral


class Salesman(Neutral):

    def __init__(self, name, level, coords, inventory):
        Neutral.__init__(self, "salesman", level, coords)
        self._inventory = inventory
        # random inventory depending on level

    def sell(self, item):
        pass
