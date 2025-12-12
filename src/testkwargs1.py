class Character:
    def __init__(self, name="", level=None, **kwargs):
        self.name = name
        self.level = level
        self.other_att = kwargs

    def describe(self):
        print(f"===Character===")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        for key, value in self.other_att.items():
            print(f"{key}:{value}")


class Warrior(Character):
    def __init__(self, name="", level=None, strength=None, **kwargs):
        super().__init__(name=name, level=level, **kwargs)
        self.strength = strength

    def describe(self):
        super().describe()
        print(f"Strength: {self.strength}")


class Mage(Character):
    def __init__(self, name="", level=None, mana=None, **kwargs):
        super().__init__(name=name, level=level, **kwargs)
        self.mana = mana

    def describe(self):
        super().describe()
        print(f"Mana: {self.mana}")


character_one = Mage(
    name="Alex", level=20, mana=40, special_ability="Summon sprites every turn"
)
character_one.describe()
