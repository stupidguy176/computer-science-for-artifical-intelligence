import termcolor

from logic import *
# we'll start with a very popular board game in the US and the UK,
# known as Clue.
# there are a number of different people
# There are a number of different rooms
# And there are a number of different weapons
# And three of these -- one person, one room, and one weapon--
# is the solution to the mystery--
# the murderer and what room they were in, and what weapon they happen to use.

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

# at the beginning of the game is that all these cards are
# randomly shuffled together, and three of them-- one person, one room,one weapon--
# are placed into a sealed envelope that we don't know.
# And we would like to figure out, using some sort of logical process, what's
# inside the envelope.
# Which person, which room, and which weapon.
symbols = characters + rooms + weapons


# And now I also have this check knowledge function.
# And what the check knowledge function does is it takes my knowledge,
# and it's going to try and draw conclusions about what I know.
def check_knowledge(knowledge):
    for symbol in symbols: # we'll loop over all of the possible symbols
        if model_check(knowledge, symbol): # Do I know that that symbol is true?
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)): #If we're not sure that the symbol is true, maybe I can check to see if I'm sure that the symbol is not true.Like, if I know for sure that it is not Professor Plum, for example.
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)
# print(knowledge.formula())
# check_knowledge(knowledge)

# Initial cards
knowledge.add(And(
    Not(mustard), Not(kitchen), Not(revolver)
))

# Unknown card
knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

# Known cards
knowledge.add(Not(plum))
knowledge.add(Not(ballroom))

check_knowledge(knowledge)
