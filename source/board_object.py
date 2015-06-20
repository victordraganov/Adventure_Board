class BoardObject:
    """
        BoardObject represents a single object placed on the board.
        Only objects such as Building or Obstacle can have size greater than
        (1,1) i.e. one field.
    """
    def __init__(self, level, coords, size):
        self._coords = coords
        self._size = size

    @property
    def size(self):
        return self._size
    
    @property
    def coords(self):
        return self._coords
    