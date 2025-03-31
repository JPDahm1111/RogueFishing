#RogueFishing player stats and statuses management file

#This file controls the player and their attributes

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me

#imports
from __future__ import annotations

from typing import TYPE_CHECKING
import color

#added
import random

from components.base_component import BaseComponent

from render_order import RenderOrder

if TYPE_CHECKING:
    from entity import Actor

#this allows "classes" to be created and player/actor attributes to be managed

    
class Fighter(BaseComponent):
    parent: Actor
    def __init__(self, hp: int, base_defense: int, base_power: int):
        self.max_hp = hp
        self._hp = hp
        self.base_defense = base_defense
        self.base_power = base_power

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))
        if self._hp == 0 and self.parent.ai:
            self.die()

    @property
    def defense(self) -> int:
        return self.base_defense + self.defense_bonus

    @property
    def power(self) -> int:
        return self.base_power + self.power_bonus

    @property
    def defense_bonus(self) -> int:
        if self.parent.equipment:
            return self.parent.equipment.defense_bonus
        else:
            return 0

    @property
    def power_bonus(self) -> int:
        if self.parent.equipment:
            return self.parent.equipment.power_bonus
        else:
            return 0

    #allows players and npcs to die, chooses from multiple possible messages and prints them to the log
    def die(self) -> None:
        #by me :0
        RandInt1 = random.randint(1, 12)
        RandInt2 = random.randint(1, 11)
        
        if self.engine.player is self.parent:
            if RandInt2 == 1:
                death_message = "As your last breath escapes your mangled body, only one light remains in the void that engulfs you: hope."
                death_message_color = color.player_die
            
            elif RandInt2 == 2:
                death_message = "You choked on fear and made a grave error. There is always a next chance!"
                death_message_color = color.player_die

            elif RandInt2 == 3:
                death_message = "They just got lucky, you'll be better next time."
                death_message_color = color.player_die

            elif RandInt2 == 4:
                death_message = "The pain is so intense that you lose consiousness for the last time, at least in this life."
                death_message_color = color.player_die
                
            elif RandInt2 == 5:
                death_message = "Final memories of the surface flash before your eyes, hopefully when you return the radiation will be gone."
                death_message_color = color.player_die

            elif RandInt2 == 6:
                death_message = "You did so well, I'm proud of you. I'll see you next time."
                death_message_color = color.player_die

            elif RandInt2 == 7:
                death_message = "No one said it would be easy, you need to try harder, you can do it!"
                death_message_color = color.player_die       

            elif RandInt2 == 8:
                death_message = "The human body can only take so much: what's left of you lifelessly slumps to the ground. You'll be back though. "
                death_message_color = color.player_die
            
            elif RandInt2 == 9:
                death_message = "Time has Little to do With Infinity and Jelly Dougnuts."
                death_message_color = color.player_die

            elif RandInt2 == 10:
                death_message = "You see your loved ones in the beautiful sunlight. One day you'll get to the surface for real."
                death_message_color = color.player_die

            elif RandInt2 == 11:
                death_message = "Death smiles at us all. All a man can do is smile back."
                death_message_color = color.player_die
            
                
           
            
        else:
            if RandInt1 == 1:
                death_message = f"{self.parent.name} won't be able to fulfill their dreams."
                death_message_color = color.enemy_die
            elif RandInt1 == 2:
                death_message = f"{self.parent.name} is dead. You did this."
                death_message_color = color.enemy_die
            elif RandInt1 == 3:
                death_message = f"You didn't let {self.parent.name} run."
                death_message_color = color.enemy_die
            elif RandInt1 == 4:
                death_message = f"{self.parent.name} was alive just a moment ago, not anymore thanks to you."
                death_message_color = color.enemy_die
            elif RandInt1 == 5:
                death_message = f"{self.parent.name} tried to stop you, it was self defense, right?"
                death_message_color = color.enemy_die
            elif RandInt1 == 6:
                death_message = f"{self.parent.name}'s flailing about finally stops. Did you make the right choice?"
                death_message_color = color.enemy_die
            elif RandInt1 == 7:
                death_message = f"You murdered {self.parent.name}, they'll haunt you for the rest of your lives."
                death_message_color = color.enemy_die
            elif RandInt1 == 8:
                death_message = f"You are covered with {self.parent.name}'s remains, disgusting."
                death_message_color = color.enemy_die
            elif RandInt1 == 9:
                death_message = f"It was you or {self.parent.name}. You were stronger."
                death_message_color = color.enemy_die
            elif RandInt1 == 10:
                death_message = f"You kill {self.parent.name} for the empire."
                death_message_color = color.enemy_die
            elif RandInt1 == 11:
                death_message = f"You thought {self.parent.name} was stronger."
                death_message_color = color.enemy_die
            elif RandInt1 == 12:
                death_message = f'"How many more will I have to kill" you think to yourself as you finish off {self.parent.name}.'
                death_message_color = color.enemy_die
        
        #creates "corpse"
        self.parent.char = "%"
        self.parent.color = (191, 0, 0)
        self.parent.blocks_movement = False
        self.parent.ai = None
        self.parent.name = f"What remains of {self.parent.name}, do you feel guilt?"
        self.parent.render_order = RenderOrder.CORPSE
        
        self.engine.message_log.add_message(death_message, death_message_color)
        self.engine.player.level.add_xp(self.parent.level.xp_given)

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
    
#goofy new damage formula
    def take_damage(self, amount: int) -> None:
    # Calculate the effective damage by subtracting defense from the incoming damage
        effective_damage = max(0, amount - self.defense)  

    # Subtract the effective damage from the player's health
        self.hp -= effective_damage

