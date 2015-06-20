from board_object import BoardObject


class Item(BoardObject):  # Abstract
    """
    Item represents a single item. It can be picked up and used depending on 
    it's purpose. When dropped an item is destroyed forever.
    size_in_inventory represents how much space the item takes in inventory.
    """

    def __init__(self, size_in_inventory, level):
        BoardObject.__init__(self, coords, (1, 1))
        self._size_in_inventory = size_in_inventory
