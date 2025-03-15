#JPD
#RogueFishing general ai management file
#This file controls the various ai types

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code by "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me (JPD)


#comments after entries are NOT by me, comments noted by """ are also not by me.
#my comments are (for the most point)above lines!
#for files with lots of comments by the original creator, I will denote their comments with ##

#imports
from __future__ import annotations

from typing import List, Tuple, TYPE_CHECKING

import numpy as np  ## type: ignore <- that isnt by me, for ex
import tcod

from actions import Action, MeleeAction, MovementAction, WaitAction


if TYPE_CHECKING:
    from entity import Actor

#sets up default, basic ai
class BaseAI(Action):
    
    def perform(self) -> None:
        raise NotImplementedError()

    def get_path_to(self, dest_x: int, dest_y: int) -> List[Tuple[int, int]]:
        """Compute and return a path to the target position.

        If there is no valid path then returns an empty list.
        """
        ## Copy the walkable array.
        cost = np.array(self.entity.gamemap.tiles["walkable"], dtype=np.int8)

        for entity in self.entity.gamemap.entities:
            ## Check that an enitiy blocks movement and the cost isn't zero (blocking.)
            if entity.blocks_movement and cost[entity.x, entity.y]:
                ## Add to the cost of a blocked position.
                ## A lower number means more enemies will crowd behind each other in
                ## hallways.  A higher number means enemies will take longer paths in
                ## order to surround the player.
                cost[entity.x, entity.y] += 10

        ## Create a graph from the cost array and pass that graph to a new pathfinder.
        graph = tcod.path.SimpleGraph(cost=cost, cardinal=2, diagonal=3)
        pathfinder = tcod.path.Pathfinder(graph)

        pathfinder.add_root((self.entity.x, self.entity.y))  # Start position.

        ## Compute the path to the destination and remove the starting point.
        path: List[List[int]] = pathfinder.path_to((dest_x, dest_y))[1:].tolist()

        ## Convert from List[List[int]] to List[Tuple[int, int]].
        return [(index[0], index[1]) for index in path]

#sets up a specialized hostile ai that is based off the basic one created above, usable for any enemy!
#additional ai types can be created and placed here!
class HostileEnemy(BaseAI):
    def __init__(self, entity: Actor):
        super().__init__(entity)
        self.path: List[Tuple[int, int]] = []

    def perform(self) -> None:
        target = self.engine.player
        dx = target.x - self.entity.x
        dy = target.y - self.entity.y
        #sketchy math stuff
        distance = max(abs(dx), abs(dy))  ## Chebyshev distance.

        if self.engine.game_map.visible[self.entity.x, self.entity.y]:
            if distance <= 1:
                return MeleeAction(self.entity, dx, dy).perform()

            self.path = self.get_path_to(target.x, target.y)

        if self.path:
            dest_x, dest_y = self.path.pop(0)
            return MovementAction(
                self.entity, dest_x - self.entity.x, dest_y - self.entity.y,
            ).perform()

        return WaitAction(self.entity).perform()

#end of line
