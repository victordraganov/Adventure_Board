class Board(object):

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self.init_field_matrix(width, height)

    def init_field_matrix(self, width, height):
        self._fields = list[height]
        for x in xrange(0, height):
            self._fields[x] = list[width]

    def get_field(self, x, y):
        return self._fields[y][x]