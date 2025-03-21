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
from components import consumable
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
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
    level=Level(level_up_base=200),
)

orc = Actor(
    char="}",
    color=(63, 127, 63),
    name="Feral Human",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)
troll = Actor(
    char="~",
    color=(0, 127, 0),
    name="Cave Horror",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

health_potion = Item(
    char="|",
    color=(255, 255, 255),
    name="Bandages",
    consumable=consumable.HealingConsumable(amount=4),
)

Single_Shot_Musket = Item(
    char="↔",
    color=(165, 42, 42),
    name="Single Shot Handgun",
    consumable=consumable. SingleShotMusket(damage=12, maximum_range=5),
)

Single_Shot_Blunderbuss = Item(
    char="`",
    color=(255, 0, 0),
    name="Single Shot Blunderbuss",
    consumable=consumable.SingleShotBlunderbuss(damage=10, radius=3),
)
