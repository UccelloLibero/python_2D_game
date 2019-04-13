"""Dungeon Game
Explore a dungeon to find a hidden door and escape. But be careful!
The grue is hiding somewhere inside!

Created: 2019
Author: Maya Husic
"""

import os
import random

# Create a game with a 2-dimensional map. Place the player, a door, and a monster into random spots in your map. Let the player move around in the map and, after each move, tell them if they've found the door or the monster. If they find either the game is over. The door is the win condition, the monster is the lose condition.

# draw the grid -- cells of the grid can maybe be tuples, rows and colums
# pick random location for player
# pick random location for the exit door
# pick random location for the monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# check for win/loss
# clear screen and redraw grid

CELLS = [
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
    (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
]
# Each item in the grid is a tuple of the coordinates for where the player is and the entire thing is a list.

def clear_screen():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations(cells):
    """Randomly pick starting locations for the monster, the door,
    and the player

    >>> cells = build_cells(2, 2)
    >>> m, d, p = get_locations(cells)
    >>> m != d and d != p
    True
    >>> d in cells
    True

    """
    monster = random.choice(cells)
    door = random.choice(cells)
    player = random.choice(cells)

    if monster == door or monster == player or door == player:
        monster, door, player = get_locations(cells)

    return monster, door, player


def random_locations():
    return random.sample(CELLS, 3)

    # above is a tuple, so maybe use packing/unpacking for this one

def move_player(player, move):
    """Based on the tuple of player's current location, move player
    to a chosen location and update it's nee location

    >>> move_player({'location': (1, 1), 'path': []}, 'LEFT')
    (0, 1)

    """
    x, y = player
    if move == 'LEFT':
        x -= 1
    if move == 'RIGHT':
        x += 1
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1
    # get the player's location
    # if move == LEFT, x-1
    # if move == RIGHT, x+1
    # if move == UP, y-1
    # if move == DOWN, y+1
    return x, y


def get_moves(player):
 """Based on the tuple of player's location, return the list of
    acceptable moves

    >>> GAME_DIMENSIONS = (2, 2)
    >>> get_moves((0, 2))
    ['RIGHT', 'UP', 'DOWN']

    """
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    # if player's y == 0, they can't move up
    # fi player's y == 4, they can't move down
    # if player's x == 0, they can't move left
    # if player's x == 4, they can't move right
    return moves


def draw_map(player):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)



def game_loop():
    monster, door, player = random_locations()
    playing = True

    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)

        print("You are currently in the room {}!".format(player)) # fill with player position
        print("You can move {}!".format(", ".join(valid_moves))) # fill with avalaible moves
        print("Enter 'QUIT' to quit!")

        move = input("> ")
        move = move.upper()

        if move == 'QUIT':
            print("\n ** See you next time! ** \n")
            break
        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print("\n ** Oh no! The monster got you! Better luck next time! ** \n")
                playing = False
            if player == door:
                print("\n ** You escaped! Congratulations!!! ** \n")
                playing = False
        else:
            input("\n ** Walls are hard! Don't run into them! **\n")

    else:
        if input("Play again? [Y/n] ").lower() != "n":
            game_loop()



        # Good move? Change the player position
        # Bad move? Don't chnage anything!
        # On the door? They win!
        # On the monster? They lose!
        # Otherwise, loop back around



clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()
