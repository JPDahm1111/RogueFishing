#JPD
#entity controller
#ALL comments by me

#this file controls ALL entities that will be used in RogueFishing

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code by "Roguelike Tutorials", website found at rogueliketutorials.com with slight addendums/modifications---------

from typing import Tuple

#basic entity template
class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
