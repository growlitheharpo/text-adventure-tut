__author__ = 'Jay'


class BaseItem():
    """The base class for all items"""

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "====== {} ======\n{}\nValue: {}".format(self.name, self.description, self.value)


class Gold(BaseItem):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front".format(str(self.amt)),
                         value=self.amt)


class Gold15(Gold):
    def __init__(self):
        super().__init__(15)


class Weapon(BaseItem):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "====== {} ======\n{}\nValue: {}\tDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)
