class BoardObject:

    """
        BoardObject represents a single object placed on the board.
        Only objects such as Building or Obstacle can have size greater than
        (1,1) i.e. one field.
    """

    def __init__(self, name, level, coords, size):
        self._coords = coords
        self._size = size

    @property
    def type(self):  # Abstract
        pass

    @property
    def name(self):
        return self._name

    @property
    def level(self):
        return self._level

    @property
    def coords(self):
        return self._coords

    @property
    def size(self):
        return self._size
