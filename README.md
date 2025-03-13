<ins>**Made by JPD for the AP Computer Science Principals 2025 Create Task**</ins>
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<ins>**About RogueFishing's Gameplay (or what I aspire for it to be)**</ins>
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
RogueFishing is an ASCII classic roguelike that draws inspiration from the original Rogue (1980) and other roguelikes like Nethack, but with a twist: fishing is the primary mean of progression in the caves and will be your key to growing stronger. In RogueFishing, you will be crawling through caves fishing, collecting items, looting and fighting monsters with the goal of finding a path to the surface. 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<ins>**About RogueFishing**</ins>
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
RogueFishing is written using python and TCOD.
TCOD is an "engine" for python that makes building roguelike much easier! More information relating to TCOD can be found here: https://python-tcod.readthedocs.io/en/latest/
This project uses lots of code from Github user TStand90's rogueliketutorials.com
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<ins>**The Future**</ins>
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
I plan on turning roguefishing into more of a Roguelite similar to Dead Cells or Diablo where there is a central hub world where your progress in the caves actually transferrs over to to enhance progression.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<ins>**Changelog**</ins>
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Build naming convention:
(Month)(Day)(Year)(letter)
Ex: 010203a
“i” is representative of an initial build, or the first build of a new version. 
After “i” comes a-h then j-z
After z comes aa, bb, cc etc. (including ii) 

Versions, starting from v0.1, denote major change.
---------------------------------------------------

<ins>v0.1, 030525i - Humble Beginnings :</ins>
- Laid down the basic foundations for creating the game:
- created the player character, represented with @
- spawned the player
- made the player controllable
- made multiple specialized files to perform tasks such as drawing the player character to controlling it

<ins>v0.1, 030525a :</ins>
- Major overhaul to EVERYTHING!!!
- created new files, entity.py and engine.py responsible for setting up entities and managing them as well as creating maps respectively. 
- modified main.py to be more lightweight and delegate tasks
- created tile_types.py, this file manages tiles and tile properties
- created game_map.py which manages the game map (doesn’t draw it, that’s engine’s job)
- modified main.py to support the newly created engine and map
	- main.py’s modifications allow for a map to be created with certain parameters, like length/width!
- modified the newly created engine to support the gamemap file
- engine handles the map like this: handle_events is called to determine details about a tile and render draws it

<ins>v0.1, 030625a :</ins>
- changed changelog from rtf to txt
- updated changeling build convention info

<ins>v0.1, 030725a :</ins>
- Modified "dejavu" font elements, characters changed:
	- @, changed to a character
	- $, changed to fish

<ins>v0.11, 030825i - Procedural Generation :</ins>
- Functional procedural map generation is implemented!
- addeded procgen.py to handle procedural generation
- modified main.py to accomidate procgen
- modified game_map.py to accomidate procgen
- The game will now procedurally generate a map when main.py is run. The player will be intellignetly placed on a valid tile.

<ins>v0.11, 030925a - FOV and Fog of War</ins> :
- modified game_map.py (using arrays) calculates FOV and stores discovered portions of the caves, this heavily utilizes TCOD features!
- modified tyle_types.py to add new "light" and "dark" tiles, these tiles are for parts of the dungeon that have been discovered or are yet to be discovered/ in sight and out of sight
- added shroud which acts as a fog of war for undiscovered parts
- modified the game engine to support the new light and dark tiles as well as the shroud mechanic

<ins>v0.11, 031025a - Intelligent entity spawning :</ins>
- Entities now spawn inside rooms!
- Basic framework for attacks and enemy moves set up!
- Modified engine.py to accomidate new entities
- modified main.py to remove placeholder entities and old spawning system
- modified engine.py to remove entity rendering
	- gamemap.py now is responisble for this
- modified procgen.py to associate the player with entities 
- added new parameters to the procgen system in main.py (max entities per room)
- Modified entity.py to support the new entity spawning system
- created entity_factories.py, which acts as a conduit for entities and allows for the various entities to be defined and customized! 
- added basic melee attack abilities in actions.py
- changed action type in input_handlers.py from "MovementAction" to "BumpAction" to support more potential interactions such as attacks

<ins>v0.11, 031125a</ins> :
- Modified fontsheet

<ins>v0.11, 031225a</ins> :
- Modified fontsheet
  
<ins>v0.12, 031225i - Ai implementation and optimizations! :</ins>
- The tutorial used some outdated syntax, these fixes should stop non fatal futureproofing 
errors
- This should also optimize the game and make it run significantly better 
- Set up groundwork for combat
- Reworked/futureproofed actions.py
- Reworked/futureproofed input_handlers.py
- Reworked/futureproofed game_map.py
- Reworked/futureproofed main.py
- Reworked/futureproofed entity.py
- Reworked/futureproofed procgen.py
- Reworked/futureproofed engine.py
- Created new components folder in the root, this contains information relating to combat and enemy ai
- Modified entity.py to accomidate new AI
- added new hostile ai framework
- modified entity_factories to add new parameters for NPC types such as ai type
- modified npc ai to only attack in 4 cardinal directions
- made attacks deal damage
- made the player and enemies able to die
- added render_order.py which allows us to determine the order in which npcs/entities are drawn
- added basic health bar
- Death config in fighter.py
- Player attribute framework in fighter.py

<ins>v0.12, 031325a</ins> :
- Modified credits across most files to be more descriptive
- Commented up the files in the folder "components" which were added in v.12 031225i
- Commented up entity_factories.py to make it's new capabilities more clear
- Modified fontsheet to add new custom entity sprites
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<ins>**Credits**</ins>
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
<ins>Python-TCOD:</ins> Copyright (c) 2009-2023, Kyle Benesch and the python-tcod contributors.
All rights reserved. Python-TCOD's Github page can be found at https://github.com/libtcod/python-tcod. Documentation for Python-TCOD can be found at https://python-tcod.readthedocs.io/en/latest/#. Python-tcod is distributed under the Simplified 2-clause FreeBSD license.
BSD 2-Clause License

Copyright (c) 2009-2023, Kyle Benesch and the python-tcod contributors.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


<ins>Roguelike Tutorials:</ins>
Most of the framework for RogueFishing was created using this tutorial, including code taken directly from it. The website for Roguelike tutorials can be found at https://rogueliketutorials.com. Roguelike tutorials was created by Tyler Standridge, and has no copyright information associated with it. 







