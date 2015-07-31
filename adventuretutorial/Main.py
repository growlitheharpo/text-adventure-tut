import world
from classes.player import Player

__author__ = 'Jay'


def play():
    world.load_tiles()
    player = Player()

    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())

    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)

        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)

            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()
    """print("Sorry, the game has been deleted.")
    world.load_tiles() """
