#JPD
#RogueFishing
#Started 3/5/25
#ALL comments by me
#written with python v 3.13.1 and tcod (a roguelike engine) v 16.2.3

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#this is the primary python file for the roguefishing project


#Imports-----------
import copy
import tcod

#import from other files
from engine import Engine
#import entity file
import entity_factories
#import the game map file
from input_handlers import EventHandler
from procgen import generate_dungeon

#Used code by "Roguelike Tutorials", website found at rogueliketutorials.com with slight addendums/modifications---------
###Draws the player (@)###
def main() -> None:
    #sets screen size
    screen_width = 80
    screen_height = 50

    #General map tomfoolery and parameters
    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2
    
    #load tiles from tileset#
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    #process/recieve events
    event_handler = EventHandler()

    #spawn the player using entity factory as a reference
    player = copy.deepcopy(entity_factories.player)
    
    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player
    )



    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)

    
    #set custom tileset font and setup some windo info/create the screen
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="RogueFishing",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        
        #the main game loop
        while True:
            #modified from initial, this essentially lets the player actually spawn in the middle of the screen
            engine.render(console=root_console, context=context)


            events = tcod.event.wait()

            #Initially, there was a command that makde it so that the player "character" didnt trail
            #now it clears previously drawn @s via the engine file
            engine.handle_events(events)

  


if __name__ == "__main__":
    main()

#end of used code---------

