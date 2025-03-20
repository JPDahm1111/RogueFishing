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
Versions, starting from v0.1, denote major change.</br>

**<ins>Full changelog available in Changelog.txt</ins>**</br>
**<ins>Current Version:</ins>**</br>
v0.12, 031925a - Save Files
- added new colors to color.py
- added new action handler system to input_handlers.py, this part is completely above me but it should allow for save file stuff to work.
- modified main.py to support new menus/saves n such
- added new file: setup_game.py
	- this file manages the main menu!
- modified engine.py to support new save system
- removed parameters from main.py
	- generally trimmed main.py down significantly 
- added save and load functions to setup_game.py
- added lzma, pickle andddddd traceback to support file saving/loading
- created RogueFishing.gitignore for my own dev uses
- Game setup parameters moved to setup_game.py
- TO DO: 
	- make menu nicer
	- random splash text!
	- make the menu screen art not look god awful
	- make more sprites
	- make placeholder friendly NPC using confused AI
	- make musket use different mechanics (current ones are abysmal lol)
 
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
Most of the framework for RogueFishing was created using this tutorial, including code taken directly from it. The website for Roguelike tutorials can be found at https://rogueliketutorials.com. Roguelike tutorials was created by Tyler Standridge, and is licensed under Creative Commons Legal Code CC0 1.0 Universal.







