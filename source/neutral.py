from board_object import BoardObject


class Neutral(BoardObject):  # Abstract

    def __init__(self, level, coords):
        BoardObject.__init__(self, level, coords, (1,1))
        self._level = level
        self._coords = coords

    @property
    def level(self):
        return self._level

    def type(self):  # Abstract
        pass

    def interact(self):  # Abstract
        pass
