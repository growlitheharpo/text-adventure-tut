__author__ = 'Jay'


class Actor:
    def __init__(self, hp, inventory):
        self.hp = hp
        self.inventory = inventory

    def is_alive(self):
        return self.hp > 0


class NPC(Actor):
    def __init__(self, hp, inventory, name, faction, inclination):
        super().__init__(hp, inventory)
        self.name = name
        self.faction = faction
        self.inclination = inclination


class Animal(NPC):
    def __init__(self, hp, inventory, name, inclination, damage):
        super().__init__(hp, inventory, name, "ANIMALS", inclination)
        self.damage = damage