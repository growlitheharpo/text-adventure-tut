__author__ = 'Jay'

import classes.tiles
import xml.etree.cElementTree as ElementTree

_world = {}


def load_tiles():
    """ Parses a file that describes the world space into the _world object """

    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')  # Might have to change '\n' to '\r\n'
            if tile_name == '':
                _world[(x, y)] = None
            else:
                _world[(x, y)] = getattr(classes.tiles, tile_name)(x, y)


def _get_tile(tile_id):
    tree = ElementTree.parse('resources/map.xml')
    root = tree.getroot()
    for tile in root:
        if tile.attrib['id'] == tile_id:
            root = tile
            break



    """
    tile_id_to_find = "0003"

    tree = ElementTree.parse('resources/map.xml')
    root = tree.getroot()
    for actor in root:
        if actor.attrib['id'] == tile_id_to_find:
            root = actor
            break

    if root.attrib['actors'] != 0:
        print("Room has the following actors:")
        for actor in root.iter('actor'):
            print(actor.text)
    """


def tile_exists(x, y):
    return _world.get((x, y))
