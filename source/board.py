from coords import Coords
from field import Field
from matrix import Matrix

class Board(object):

    def __init__(self, height, width):
        self._width = width
        self._height = height
        self._fields = Matrix(width, height)