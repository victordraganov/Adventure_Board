from neutral import Neutral

class Salesman(Neutral):

    def __init__(self, level, coords, inventory):
        super.__init__(level, coords)
        self._inventory = inventory

    def sell(self, item):
        pass

    def type(self):
        return "salesman"