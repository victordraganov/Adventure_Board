from neutral import Neutral

class Gambler(Neutral):

    def __init__(self, level, coords):
        super.__init__(level, coords)

    def gamble_money(self, money):
        pass

    def type(self):
        return "gambler"