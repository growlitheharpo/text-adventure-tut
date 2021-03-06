__author__ = 'Jay'

import classes.items
import classes.enemies
import actions
import world


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())

        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())

        return moves


class DynamicTile(MapTile):
    def __init__(self, x, y, p_actors, p_items, description, id):
        super().__init__(x, y)
        self.description = description
        self.id = id

        self.actors = []
        self.items = []

        for actor_types in p_actors:
            self.actors.append(getattr(classes.enemies, actor_types)())
            # self.actors.append(getattr(classes.enemies, actor_types))()

        for item_types in p_items:
            self.items.append(getattr(classes.items, item_types)())

    def intro_text(self):
        return self.description

    def modify_player(self, player):
        pass  # TODO: will later need to implement interacting with actors and items (should anything be here??)

    def available_actions(self):
        base_actions = super().available_actions()

        if len(self.actors) > 0:
            for i in range(0, len(self.actors)):
                print(str(i + 1) + ". Speak to " + str(self.actors[i]))

        return base_actions


class StartingRoom(MapTile):
    def intro_text(self):
        return """
            You find yourself in a cave with a flickering torch on the wall.
            You can make out four paths, each equally as dark and foreboding.
            """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining".format(self.enemy.damage, player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile = self), actions.Attack(enemy=self.enemy)]
        else:
            return super().available_actions()


class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
            Another unremarkable part of the cave. You must forge onwards.
            """

    def modify_player(self, player):
        # Room has no action on player
        pass


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, classes.enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return "A giant spider jumps down from its web in front of you!"
        else:
            return "The corpse of a dead spider rots on the ground."


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, classes.items.Dagger())

    def intro_text(self):
        return "You notice something shiny in the corner.\nIt's a dagger! You pick it up."


class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
            You see a bright light in the distance...
            ... it grows as you get closer. It's sunlight!

            Victory is yours!
            """

    def modify_player(self, player):
        player.victory = True
