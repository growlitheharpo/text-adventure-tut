__author__ = 'Jay'

from classes.actor import NPC
from classes.actor import Animal

import classes.items


class GiantSpider(Animal):
    def __init__(self):
        super().__init__(hp=10, inventory=[], name="Giant Spider", inclination=0, damage=2)


class Ogre(Animal):
    def __init__(self):
        super().__init__(hp=30, inventory=[], name="Ogre", inclination=0, damage=15)


class BaseMerchant(NPC):  # in the enemy file because fuck economics
    def __init__(self):
        super().__init__(hp=50, inventory=[classes.items.Gold(500)], name="George", faction="MERCHANTS", inclination=10)
