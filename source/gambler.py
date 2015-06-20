from neutral import Neutral

# If player is lower level than the gambler his luck must be reduced
class Gambler(Neutral):

    def __init__(self, level, coords):
        Neutral.__init__(self, level, coords)

    def gamble_money(self, money):
        pass
    #   GAMBLER WILL PROPOSE A DICE GAME OF "PIG"(1 OR 2 DICE)

    def type(self):
        return "gambler"
