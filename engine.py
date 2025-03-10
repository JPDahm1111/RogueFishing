#JPD
#RogueFishing engine 


#This engine file is responsible for creating the map and managing entities

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code by "Roguelike Tutorials", website found at rogueliketutorials.com with slight addendums/modifications---------

#imports

from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov
from entity import Entity
#add gamemap support
from game_map import GameMap
from input_handlers import EventHandler

#This first bit manages the player and creates a pseudo list exclusive to TCOD that handles entities.
#the pseudo list ensures one entity cannot be added to it multiple times
class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player
        self.update_fov()
        

    #This iterates through events
    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue
            #modified to support gamemap as of 030525a
            #calls to actions 
            action.perform(self, self.player)

            self.update_fov()  # Update the FOV before the players next action.

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    #draws entities and tiles
    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)
        
        for entity in self.entities:
            # Only print entities that are in the FOV
            if self.game_map.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg=entity.color)


        context.present(console)

        console.clear()
