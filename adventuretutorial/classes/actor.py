__author__ = 'Jay'

import consts as CONST


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

    def __str__(self):
        return self.name


class Animal(NPC):
    def __init__(self, hp, inventory, name, inclination, damage):
        super().__init__(hp, inventory, name, CONST.ANIMAL_FACTION, inclination)
        self.damage = damage
