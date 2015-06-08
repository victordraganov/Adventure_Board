class Field(object):

    def __init__(self, coords):
        self._coords = coords

    @property
    def occupied(self):
        return self._occupied
    