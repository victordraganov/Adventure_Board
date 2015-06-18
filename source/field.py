class Field(object):
    def __init__(self, coords):
        self._coords = coords
        self._occupier = None
    
    def occupied(self):
        return self._occupier == None
    
    def assign_occupier(self, object_name):
        self._occupier = object_name

    def occupier(self):
        return self._occupier
