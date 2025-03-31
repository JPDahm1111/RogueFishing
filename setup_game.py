#game setup file 

#This file acts as a game initialization/setup screen. It basically is the main menu.

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me

#imports

"""Handle the loading and initialization of game sessions."""
from __future__ import annotations

import copy
import lzma
import pickle
import traceback
from typing import Optional
import tcod
import color
from engine import Engine
import entity_factories
from game_map import GameWorld
import input_handlers
import random


# Load the background image and remove the alpha channel.
background_image = tcod.image.load("New Piskel.png")[:, :, :3]

#This is now where the game is configured!!!!!!
#moved from main
def new_game() -> Engine:
    """Return a brand new game session as an Engine instance."""
    map_width = 80
    map_height = 43

    room_max_size = 12
    room_min_size = 2
    max_rooms = 45


    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_world = GameWorld(
        engine=engine,
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,

    )
    engine.game_world.generate_floor()
    engine.update_fov()
#randomize this
    engine.message_log.add_message(
        "You regain consiousness in the caves. Again. Maybe this time you'll reach the surface.", color.welcome_text
    )
#autoequip weapons
    Shortsword = copy.deepcopy(entity_factories.Shortsword)
    Gambeson = copy.deepcopy(entity_factories.Gambeson)

    Shortsword.parent = player.inventory
    Gambeson.parent = player.inventory

    player.inventory.items.append(Shortsword)
    player.equipment.toggle_equip(Shortsword, add_message=False)

    player.inventory.items.append(Gambeson)
    player.equipment.toggle_equip(Gambeson, add_message=False)
    return engine

#load function
def load_game(filename: str) -> Engine:
    """Load an Engine instance from a file."""
    with open(filename, "rb") as f:
        engine = pickle.loads(lzma.decompress(f.read()))
        assert isinstance(engine, Engine)
    return engine


class MainMenu(input_handlers.BaseEventHandler):
    """Handle the main menu rendering and input."""

    def on_render(self, console: tcod.Console) -> None:
        """Render the main menu on a background image."""
        console.draw_semigraphics(background_image, 0, 0)

#print the title of the game
        console.print(
            console.width // 2,
            console.height // 2 - 4,
            "RogueFishing",
            fg=color.menu_title,
            alignment=tcod.CENTER,
        )

#entirely by me vvv
        # Display random splash text
        console.print(
            console.width // 2,
            console.height - 2,
            #calls splash text func
            st_procgen(),  
            fg=color.menu_title,
            alignment=tcod.CENTER,
        )
#entirely by me ^^^
            
#These are options to start the game/ quit it!
        menu_width = 24
        for i, text in enumerate(
            ["[N] Play a new game", "[C] Continue last game", "[Q] Quit"]
        ):
            console.print(
                console.width // 2,
                console.height // 2 - 2 + i,
                text.ljust(menu_width),
                fg=color.menu_text,
                bg=color.black,
                alignment=tcod.CENTER,
                bg_blend=tcod.BKGND_ALPHA(64),
            )

    def ev_keydown(
        self, event: tcod.event.KeyDown
    ) -> Optional[input_handlers.BaseEventHandler]:
        if event.sym in (tcod.event.K_q, tcod.event.K_ESCAPE):
            raise SystemExit()
        elif event.sym == tcod.event.K_c:
            try:
                return input_handlers.MainGameEventHandler(load_game("savegame.sav"))
            except FileNotFoundError:
                return input_handlers.PopupMessage(self, "No saved game to load.")
            except Exception as exc:
                traceback.print_exc()  # Print to stderr.
                return input_handlers.PopupMessage(self, f"Failed to load save:\n{exc}")
        elif event.sym == tcod.event.K_n:
            return input_handlers.MainGameEventHandler(new_game())

        return None
    
#entirely by me vvv
#splash text list
splashtexts = [
    "Fishtastic",
    "Fish not included!",
    "Infinite!?",
    "Replay value!",
    "Time has little to do with infinity and jelly doughnuts!",
    "Also try...I haven't really made anything else!",
    "The peak of roguelikes!",
    "Fishing? Not yet!",
    "0.35 is Water!",
    "Don't cave straight down!",
    "Reach the surface!",
    "If you make any input, I'll change!",
    "Made by me... for the most part!",
    "I am Steve!",
    "Deep combat!",
    "Mouse not included!",
    "Hardcore mode? We're in UltraHardcore mode!",
    "I yearn for the depths!",
    "Breathe out before going through tight squeezes!",
    "Press > to ascend!",
    "Tutorials are for the weak (I'm not lazy I swear)",
    "proper, grammer!",
    "No language support!",
    "Edgy!",
    "AP Computer Science Principals!",
    "Shoutout to my teacher!",
    "At least one gameplay mechanic!",
    "No mining OR crafting!",
    '"Shift" will not make you sprint!',
    "The impala is NOT tame!",
    "Lots of foes!",
    "Web fishing (but not on the web)!",
    "Gaben was not here!",
    "Wake up samurai, we've got a fish to catch!",
    "Better than Skyrim!",
    "The rocks were tricked into thinking!",
    "Philisophically deep",
    "Do NOT eat Plato!",
    "I think therefore I fish!",
    "The west has risen! Billions must fish!",
    "Unfinished? More like full of potential!",
    "Back in monochrome!",
    "Who needs fancy graphics when you have font?!",
    "The fewer the merrier!",
    "Fear the walking fish!",
    "Fishing Time!",
    "The fishing game with NO fishing Mechanics!",
    "Tilde does not open console!",
    "I'll lock in 2026!",
    "This is a list!",
    "Pure organic Python!",
    "Wholesome!",
    "We need to Fish!",
    "Have fun!",
    ":D",
    "If I can do this, you can too!",
    "What doth life?",
    "I like trains!",
    "Your adventure begins here (until you ragequit)!",
    "Now with saving!",
    "Contains no caffiene!",
    "Diet!",
    "It's a bittersweet roguelike this game!",
    "Do not consume!",
    "A set tone, what's that?!",
    "Fishing. Fishing never changes!",
    "Now with Mac support!",
    "Don't mind the bugs!",
    "Don't worry, be happy!",
    "Everything will be alright if you let it go!",
    "I see a red door and I want it painted in RGB!",

]
def st_procgen():
    return random.choice(splashtexts)
#entirely by me ^^^

