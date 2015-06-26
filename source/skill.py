class Skill:

    """
        Represents a special skill which can be learned by a hero from a 
        certain category. Skills can be "active" or "passive" types.
        Active skills make damage to enemies. Passive make something useful 
        for the hero himself or teammate.
    """

    def __init__(self, name, hero_category, skill_type):
        self._name = name
        self._category = hero_category
        self._skill_type = skill_type

    @property
    def name(self):
        return self._name

    @property
    def hero_category(self):
        return self._hero_category

    @property
    def skill_type(self):
        return self._skill_type
