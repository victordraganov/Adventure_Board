from board_object import BoardObject


class Neutral(BoardObject):  # Abstract

    def __init__(self, name, level, coords):
        BoardObject.__init__(self, name, level, coords, (1,1))

    def type(self):  # Abstract
        pass

    def interact(self):  # Abstract
        pass
