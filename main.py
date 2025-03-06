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
import tcod

#import from other files
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

#Used code by "Roguelike Tutorials", website found at rogueliketutorials.com with slight addendums/modifications---------
###Draws the player (@)###
def main() -> None:
    #sets screen size
    screen_width = 80
    screen_height = 50

    #spawn the player in the middle of the screen
    player_x = int(screen_width // 2)
    player_y = int(screen_height // 2)
    
    #load tiles from tileset#
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    #process/recieve events
    event_handler = EventHandler()
    
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
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)

            #This command makes it so that the player "character" doesnt trail
            #it clears previously drawn @s!
            root_console.clear()
            
            #"for event" is a general event handler!
            for event in tcod.event.wait():

                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()

  


if __name__ == "__main__":
    main()

#end of used code---------

