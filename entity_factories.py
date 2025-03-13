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
from components.fighter import Fighter
from entity import Actor

#These options allow entities to be created and customized!
#entitiy visual appearance and gameplay attributes customizable! yipeeee!

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    #because player doesn't use ai this is useless vvv
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)
