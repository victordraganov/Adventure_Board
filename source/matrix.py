
    """
        Matrix represents 2d array.
        When first initialized all elements are None.
    """

    def __init__(self, height, width):
        self._2d_array = []
        self._init_matrix(height, width)
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    def _init_matrix(self, height, width):
        for i in range(0, height):
            self._2d_array.append([])
            for j in range(0, width):
                self._2d_array[i].append(None)

    # X is for the horizontal and Y is for the vertical axis.
    def get(self, x, y):
        if x > self.width or y > self.height or x < 0 or y < 0:
            raise "Invalid index in get() function!"
        return self._2d_array[y][x]
