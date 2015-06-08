class Neutral(object): # Abstract

    def __init__(self, level, coords):
        super.__init__(level, coords)

    def type(self): # Abstract
        pass

    def interact(self): # Abstract
        pass