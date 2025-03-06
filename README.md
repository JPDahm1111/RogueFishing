Made by JPD for the AP Computer Science Principals 2025 Create Task
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
About RogueFishing's Gameplay (or what I aspire for it to be)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
RogueFishing is an ASCII classic roguelike that draws inspiration from the original Rogue (1980) and other roguelikes like Nethack, but with a twist: quicktime based fishing (similarly to that of Animal Crossing or Webfishing) is the primary mean of progression through the caves. In RogueFishing, you will be crawling through caves fishing, collecting items, looting and fighting monsters with the goal of finding a path to the surface. 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
About RogueFishing
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
RogueFishing is written using python and TCOD.
TCOD is an "engine" for python that makes building roguelike much easier! More information relating to TCOD can be found here: https://python-tcod.readthedocs.io/en/latest/
This project uses lots of code from Github user TStand90's rogueliketutorials.com
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The Future
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
I plan on turning roguefishing into more of a Roguelite similar to Dead Cells or Diablo where there is a central hub world where your progress in the caves actually transferrs over to to enhance progression.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Changelog
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Build naming convention:
(Month)(Day)(Year)(letter)
Ex: 010203a
“i” is representative of an initial build, or the first build of a new version. 
After “i” comes a-h then j-z
After z comes aa, bb, cc etc. (including ii) 

Versions, starting from v0.1, denote major change.
—————————————————————————————————————————————------

v0.1, 030525i :
Laid down the basic foundations for creating the game:
-created the player character, represented with @
-spawned the player
-made the player controllable
-made multiple specialized files to perform tasks such as drawing the player character to controlling it

v0.1, 030525a :
Major overhaul to EVERYTHING!!!
-created new files, entity.py and engine.py responsible for setting up entities and managing them as well as creating maps respectively. 
-modified main.py to be more lightweight and delegate tasks
-created tile_types.py, this file manages tiles and tile properties
-created game_map.py which manages the game map (doesn’t draw it, that’s engine’s job)
-modified main.py to support the newly created engine and map
	-main.py’s modifications allow for a map to be created with certain parameters, like length/width!
-modified the newly created engine to support the gamemap file
- engine handles the map like this: handle_events is called to determine details about a tile and render draws it
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Credits
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Python-TCOD: Copyright (c) 2009-2023, Kyle Benesch and the python-tcod contributors.
All rights reserved. Python-TCOD's Github page can be found at https://github.com/libtcod/python-tcod. Documentation for Python-TCOD can be found at https://python-tcod.readthedocs.io/en/latest/#.

Roguelike Tutorials, the website for Roguelike tutorials which I use code from in this project, can be found at https://rogueliketutorials.com






