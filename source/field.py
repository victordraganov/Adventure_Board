class Field(object):

    """
        Every field points to a BoardObject which is it's occupier.
        If the field is empty then the occupier is None value.
        The Field itself does not represent a BoardObject.
    """

    def __init__(self, coords):
        self._coords = coords
        self._occupier = None

    def occupied(self):
        return self._occupier == None

    def assign_occupier(self, object_name):
        self._occupier = object_name

    def occupier(self):
        return self._occupier
