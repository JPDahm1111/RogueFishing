#RogueFishing engine 


#This engine file is responsible for creating the map and managing entities

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me

#imports

from __future__ import annotations

import lzma
import pickle

from typing import TYPE_CHECKING


from tcod.console import Console
from tcod.map import compute_fov
import exceptions

from message_log import MessageLog
import render_functions

if TYPE_CHECKING:
    from entity import Actor
    from game_map import GameMap, GameWorld
    

#This first bit manages the player and creates a pseudo list exclusive to TCOD that handles entities.
#the pseudo list ensures one entity cannot be added to it multiple times
class Engine:
    game_map: GameMap
    #multiple maps achieved through caving
    game_world: GameWorld

    def __init__(self, player: Actor):
        self.message_log = MessageLog()
        self.mouse_location = (0, 0)
        self.player = player

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.actors) - {self.player}:
            if entity.ai:
                try:
                    entity.ai.perform()
                except exceptions.Impossible:
                    pass  # Ignore impossible action exceptions from AI.
                

    #This iterates through events
    
    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=8,
        )
        # If a tile is "visible" it should be added to "explored".
        self.game_map.explored |= self.game_map.visible

    #draws entities, tiles and ui
    #VERY CRUCIAL/useful!!!
    def render(self, console: Console) -> None:
        self.game_map.render(console)
        
        self.message_log.render(console=console, x=21, y=45, width=40, height=5)

        console.print(
            x=1,
            y=46,
            string=f"HP: {self.player.fighter.hp}/{self.player.fighter.max_hp}",
        )
#shows cave level and entity names
        render_functions.render_cave_level(
            console=console,
            cave_level=self.game_world.current_floor,
            location=(0, 47),
        )

        render_functions.render_names_at_mouse_location(
            console=console, x=21, y=44, engine=self
        )

#this function manages savefiles
    def save_as(self, filename: str) -> None:
        """Save this Engine instance as a compressed file."""
        save_data = lzma.compress(pickle.dumps(self))
        with open(filename, "wb") as f:
            f.write(save_data)

        
