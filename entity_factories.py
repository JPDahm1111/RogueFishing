#JPD
#additional entity controller
#ALL comments by me

#This file managies entities, specifically when they are cloned and transferred to game_map.py, additionally it allows the various entities to be defined!

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me (JPD)

#imports

from components.ai import HostileEnemy
from components.consumable import HealingConsumable
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item

#These options allow entities to be created and customized!
#entitiy visual appearance and gameplay attributes customizable! yipeeee!

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    #because player doesn't use ai this is useless vvv
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
    inventory=Inventory(capacity=26),
)

orc = Actor(
    char="}",
    color=(63, 127, 63),
    name="Fallen Fisher",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
)
troll = Actor(
    char="~",
    color=(0, 127, 0),
    name="Cave Horror",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0),
)

health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=HealingConsumable(amount=4),
)
