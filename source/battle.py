from unit import Unit
from coords import Coords


class Battle(object):

    """This class represents a single battle on the battlefield. There are two
        "teams" which will fight against each other. After the battle the dead
        allies are removed from the game. The winners return to their original
        positions on the map. Battle(list, list)
    """

    def __init__(self, left_allies, right_allies):
        self._left_allies = left_allies
        self._right_allies = right_allies
        self._left_map_coords = []
        self._right_map_coords = []
        self.extract_map_coords()

    def extract_map_coords(self):
        for ally in self._left_allies:
            self._left_map_coords.append(ally.coords)

        for ally in self._right_allies:
            self._right_map_coords.append(ally.coords)
