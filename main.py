#RogueFishing
#Started 3/5/25
#written with python v 3.13.1 and tcod (a roguelike engine) v 16.2.3

#detailed credits, including copyright information, can be found in Credits.txt

#comments noted by """ are also not by me.
#my comments are (for the most point)above lines!
#for files with lots of comments by the original creator (which is not all of them), I will denote their comments with ##

#Home screen "New Piskel.png" by me
#Font sheet "dejavu10x10_gs_tc.png" is made by the python-tcod developers with changes by me.

#credits, detailed credits can be found at credits.txt:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#Used code by "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me 

#this is the master python file for roguefishing 



#Imports-----------

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me 

import traceback
import tcod
import color
import exceptions
import input_handlers
import setup_game


#this function manages savefiles and calls them from engine.py
def save_game(handler: input_handlers.BaseEventHandler, filename: str) -> None:
    """If the current event handler has an active Engine then save it."""
    if isinstance(handler, input_handlers.EventHandler):
        handler.engine.save_as(filename)
        print("Game saved.")

def main() -> None:
    #sets screen size
    screen_width = 80
    screen_height = 50

 
    #load tiles from tileset#
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    handler: input_handlers.BaseEventHandler = setup_game.MainMenu()
    
    #set custom tileset font and setup some windo info/create the screen
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="RogueFishing",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        
        try:
            while True:
                root_console.clear()
                handler.on_render(console=root_console)
                context.present(root_console)

                try:
                    for event in tcod.event.wait():
                        context.convert_event(event)
                        handler = handler.handle_events(event)
                except Exception:  # Handle exceptions in game.
                    traceback.print_exc()  # Print error to stderr.
                    # Then print the error to the message log.
                    if isinstance(handler, input_handlers.EventHandler):
                        handler.engine.message_log.add_message(
                            traceback.format_exc(), color.error
                        )
        except exceptions.QuitWithoutSaving:
            raise
        except SystemExit:  # Save and quit.
            save_game(handler, "savegame.sav")
            raise
        except BaseException:  # Save on any other unexpected exception.
            save_game(handler, "savegame.sav")
            raise


if __name__ == "__main__":
    main()

#end of used code---------

#end of line
