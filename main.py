#JPD
#RogueFishing
#Started 3/5/25
#written with python v 3.13.1 and tcod (a roguelike engine) v 16.2.3

#comments after entries are NOT by me, comments noted by """ are also not by me.
#my comments are (for the most point)above lines!
#for files with lots of comments by the original creator, I will denote their comments with ##

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#Used code by "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me (JPD)

#this is the primary python file for the roguefishing project


#Imports-----------
import copy
import traceback
import tcod
import color

#import from other files
from engine import Engine
#import entity file
import entity_factories
#import the game map file
from procgen import generate_dungeon

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me (JPD)
###Draws the player (@)###
def main() -> None:
    #sets screen size
    screen_width = 80
    screen_height = 50

    #General map tomfoolery and parameters
    map_width = 80
    map_height = 43

    room_max_size = 14
    room_min_size = 3
    max_rooms = 33

    #mobs/items per room
    max_monsters_per_room = 2
    max_items_per_room = 2
    
    #load tiles from tileset#
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    #process/recieve events
    player = copy.deepcopy(entity_factories.player)

    #spawn the player using entity factory as a reference
    engine = Engine(player=player)
    
    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        max_items_per_room=max_items_per_room,
        engine=engine,
    )



    engine.update_fov()

    engine.message_log.add_message(
        "You enter the caves again, maybe this time you'll reach the surface.", color.welcome_text
    )
    
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
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)


            try:
                for event in tcod.event.wait():
                    context.convert_event(event)
                    engine.event_handler.handle_events(event)
            except Exception:  # Handle exceptions in game.
                traceback.print_exc()  # Print error to stderr.
                # Then print the error to the message log.
                engine.message_log.add_message(traceback.format_exc(), color.error)




if __name__ == "__main__":
    main()

#end of used code---------

#end of line

#........'''''.      ..'',,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;,..                ..';:cc::;,..           .;;;;,                   .''''''.'
#,:'........,dc    ,loc;;;,,,,,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;cod1'           'codlc:,,,,;:loxxc'      ..xx;;;dd.                 cx,....,o'
#,c.        .x:  ,ol'...                                      .,oo'      .:ol,.           ..':xkl.   ..kk. ..ckl.               cO.    'o'
#;l.        .kc cx:..     .......................................;d,   .cd:.        ...       .'oO1. .'kk.   .'lkc.             lO.    'd'
#.;,,,,,,,,;;c;'ko..   ;ddllllllllooooooooooodddddddddddddddddddxxdo. .dc.     .,:oodddxdl;.    .;kO,.'Ok.    ..'dk:.           lO.    'd'
              #,x: .   .kd............................................ol.     ,dl,......'ckOc.....,OO''OO.      ..;xx'          l0.    .d'
              #,kc .   .ko..   ....,kdlclllxd'.:kdooodddddddddddddxx':x...  .lo............1Kx.....;0d'OO.        ..cko. .......o0.    ,d'
              #,kc .   .kd..  .....:Kd.....O0,.oK;...............:kc.dc.....ck'.............1Xc.....k0,OO.          .,Ox,xc'''',':.    ,x'
              #,k: .   .kd..    ...:0d.....O0,.oK;.............;dd,..d:.....lO..............cKc.....x0,0O.    .......;0x;0:            ,x'
              #,k: .    kd..      .;0d.....O0,.,kd,.....':::cloc'....co.    ,ko............,OO.....,0x'0O.  ..ox:,,'';:''dx;           ,x,
              #,x:      ko..       ;0d.....O0'...ckd;.....'oxc........o,     .ox;.........1Ox......xK;,OO.  ..oO,       ..;xd.         ,x,
              #,x:      xo..       ;0o.   .k0'.....:xo,.....'ld;......'o'.    .'colc::cldd1'    ..xK:.'OO.  ..oO,          .cxc.       ,x'
              #,x;      xo..       ;Oo.   .k0'.     .;dd;.    .:o;.    .lc.       .......      .;Ox' .'OO.  ..lO,            .cd;      ,x'
              #,x;      xl .       ,Oo.   .k0'.       .,od;,    .:dc.    'cc'.              .'lkk;   .'Ok.  ..lO,              .ld;    ,d'
              #,d;      xl .       ,kl.   .xO..          'dd;.    .:o:.    .;ll;'........':okxc.     .'kk.  ..lk,               .'oo.  ,d,
              #.c;;''',;,          .oo::cccl:.             'ldigitalllc.      ..,;:ccllllc:'.         .:c:::::ll.                 .,,',,c.

#(logo made by Github user Mike Bell)

