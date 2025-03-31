
#additional entity controller


#This file manages entities, specifically when they are cloned and transferred to game_map.py, additionally it allows the various entities to be defined!

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me 

#imports

from components.ai import HostileEnemy
from components.ai import Static
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item, Static

#These options allow entities to be created and customized!
#entitiy visual appearance and gameplay attributes customizable! yipeeee!

#Player
player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    #because player doesn't use ai this is useless vvv
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=1, base_power=2),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

#NPC - Enemy
orc = Actor(
    char="}",
    color=(63, 127, 63),
    name="Feral Human",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=5),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)
troll = Actor(
    char="~",
    color=(0, 127, 0),
    name="Cave Horror",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=8),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

#consumable - health
health_potion = Item(
    char="|",
    color=(255, 255, 255),
    name="Bandages",
    consumable=consumable.HealingConsumable(amount=4),
)

#consumable - weapon
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

#equippables
Shortsword = Item(
    char="◄", color=(184, 115, 51), name="Training Shortsword", equippable=equippable.Shortsword()
)

ShortswordC = Item(
    char="◄", color=(255, 15, 0), name="Copper Shortsword", equippable=equippable.ShortswordC()
)

ShortswordB = Item(
    char="◄", color=(255, 15, 0), name="Bronze Shortsword", equippable=equippable.ShortswordB()
)

ShortswordI = Item(
    char="◄", color=(86, 86, 86), name="Iron Shortsword", equippable=equippable.ShortswordI()
)

ShortswordS = Item(
    char="◄", color=(211, 211, 211), name="Steel Shortsword", equippable=equippable.ShortswordS()
)

ShortswordDS = Item(
    char="◄", color=(211, 211, 211), name="Damascus Steel Shortsword", equippable=equippable.ShortswordDS()
)

Cleaver = Item(char="▼", color=(0, 191, 255), name=" Butcher's Cleaver", equippable=equippable.Cleaver()
)

Gambeson = Item(
    char="►",
    color=(128, 128, 128),
    name=" Basic Gambeson",
    equippable=equippable.Gambeson(),
)



FlakVest = Item(
    char="[", color=(139, 69, 19), name="Flak Vest", equippable=equippable.FlakVest()
)

#objects
water = Static(
    char="%",
    color=(0, 0, 255),
    name="Water",
)
