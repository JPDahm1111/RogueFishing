#Euippable file


#This file manages the ability of items to be equipped

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me 



#imports
from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    parent: Item

    def __init__(
        self,
        equipment_type: EquipmentType,
        power_bonus: int = 0,
        defense_bonus: int = 0,
    ):
        self.equipment_type = equipment_type

        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus

#manages equipment
class Shortsword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=2)


class Cleaver(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=4)


class Gambeson(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=1)


class FlakVest(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=3)
