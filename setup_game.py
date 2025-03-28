#JPD
#game setup file 
#ALL comments by me

#This file acts as a game initialization/setup screen. It basically is the main menu.

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code from "Roguelike Tutorials" created by Tyler Standridge, website found at rogueliketutorials.com with addendums/modifications by me (JPD)

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

#SPLASH TEXTTTT
#update to make this random in the future
        console.print(
            console.width // 2,
            console.height - 2,
            "Fishtastic",
            fg=color.menu_title,
            alignment=tcod.CENTER,
        )

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
