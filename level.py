#RogueFishing
#leveling file

#This file is responsible for managing leveling and its effects on the player

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me 


from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor

#default leveling info
class Level(BaseComponent):
    parent: Actor

    def __init__(
        self,
        current_level: int = 1,
        current_xp: int = 0,
        level_up_base: int = 0,
        level_up_factor: int = 150,
        xp_given: int = 0,
    ):
        self.current_level = current_level
        self.current_xp = current_xp
        self.level_up_base = level_up_base
        self.level_up_factor = level_up_factor
        self.xp_given = xp_given
#leveling equation
    @property
    def experience_to_next_level(self) -> int:
        return self.level_up_base + self.current_level * self.level_up_factor

    @property
    def requires_level_up(self) -> bool:
        return self.current_xp > self.experience_to_next_level
#leveling system
    def add_xp(self, xp: int) -> None:
        if xp == 0 or self.level_up_base == 0:
            return

        self.current_xp += xp

        self.engine.message_log.add_message(f"You learn more from the caves and gain {xp} exp.")

        if self.requires_level_up:
            self.engine.message_log.add_message(
                f"You reach a breakthrough in your knowledge and achieve level {self.current_level + 1}!"
            )

    def increase_level(self) -> None:
        self.current_xp -= self.experience_to_next_level

        self.current_level += 1

    def increase_max_hp(self, amount: int = 3) -> None:
        self.parent.fighter.max_hp += amount
        self.parent.fighter.hp += amount

        self.engine.message_log.add_message("Stress builds strength: your body has taken so many beatings you grow stronger! (+hp)")

        self.increase_level()

    def increase_power(self, amount: int = 1) -> None:
        self.parent.fighter.power += amount

        self.engine.message_log.add_message("You've killed so much you grow better at it. Is this really nessecary? (+dam)")

        self.increase_level()

    def increase_defense(self, amount: int = 1) -> None:
        self.parent.fighter.defense += amount

        self.engine.message_log.add_message("Your skin callouses and hardens, enemy blows hurt you less! (+def)")

        self.increase_level()
