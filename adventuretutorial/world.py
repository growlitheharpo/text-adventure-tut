__author__ = 'Jay'

import classes.tiles

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
            # _world[(x, y)] = None if tile_name == '' else getattr(__import__('classes.tiles'), tile_name)(x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(classes.tiles, tile_name)(x, y)


def tile_exists(x, y):
    return _world.get((x, y))
