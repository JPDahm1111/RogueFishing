#equpment types

#This file manages the various equipment types.

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me 

#imports
from enum import auto, Enum


class EquipmentType(Enum):
    WEAPON = auto()
    ARMOR = auto()
