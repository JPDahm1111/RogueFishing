#JPD
#RogueFishing exceptions file

#This file allows for special exceptions to be created and managed

#credits:
#general TCOD reference: https://python-tcod.readthedocs.io/en/latest/index.html
#roguelike tutorial: rogueliketutorials.com

#Used code by "Roguelike Tutorials", website found at rogueliketutorials.com with slight addendums/modifications---------




class Impossible(Exception):
    """Exception raised when an action is impossible to be performed.

    The reason is given as the exception message.
    """

class QuitWithoutSaving(SystemExit):
    """Can be raised to exit the game without automatically saving."""
