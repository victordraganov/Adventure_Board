class Neutral:  # Abstract

    def __init__(self, level, coords):
        self._level = level
        self._coords = coords

    @property
    def level(self):
        return self._level

    @property
    def coords(self):
        return self._coords

    def type(self):  # Abstract
        pass

    def interact(self):  # Abstract
        pass
