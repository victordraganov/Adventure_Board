class Skill:

    """
        Represents a special skill which can be learned by a hero from a 
        certain category. Skills can be "active" or "passive" types.
    """

    def __init__(self, hero_category, skill_type):
        self._category = hero_category
        self._skill_type = skill_type
