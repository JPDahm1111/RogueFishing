#JPD
#RogueFishing player stats and statuses management file



#This file controls the player and their attributes

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me (JPD)

#imports
from __future__ import annotations

from typing import TYPE_CHECKING
import color

from components.base_component import BaseComponent
from input_handlers import GameOverEventHandler
from render_order import RenderOrder

if TYPE_CHECKING:
    from entity import Actor

#this allows "classes" to be created and player/actor attributes to be managed
class Fighter(BaseComponent):
    parent: Actor
    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self._hp = hp
        self.defense = defense
        self.power = power

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.parent.ai:
            self.die()

    #allows players and npcs to die
    def die(self) -> None:
        if self.engine.player is self.parent:
            death_message = "As your last breath escapes your mangled body, only one light remains in the void that engulfs you: hope."
            death_message_color = color.player_die
            self.engine.event_handler = GameOverEventHandler(self.engine)
        else:
            death_message = f"{self.parent.name} won't be able to fulfill their dreams."
            death_message_color = color.enemy_die
        #creates "corpse"
        self.parent.char = "%"
        self.parent.color = (191, 0, 0)
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"What remains of {self.parent.name}, do you feel guilt?"
        self.parent.render_order = RenderOrder.CORPSE
        
        self.engine.message_log.add_message(death_message, death_message_color)

    #this function heals an entity!
    def heal(self, amount: int) -> int:
        if self.hp == self.max_hp:
            return 0

        new_hp_value = self.hp + amount

        if new_hp_value > self.max_hp:
            new_hp_value = self.max_hp

        amount_recovered = new_hp_value - self.hp

        self.hp = new_hp_value

        return amount_recovered

    def take_damage(self, amount: int) -> None:
        self.hp -= amount
