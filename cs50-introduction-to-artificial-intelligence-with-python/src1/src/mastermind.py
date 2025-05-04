from logic import *

# But if you've ever played games like Mastermind
# where you're trying to figure out which order different colors go in
# and trying to make predictions about it, I could tell you, for example.
# Let's play a simplified version of Mastermind where there are four
# colors-- red, blue, green, and yellow--
# and they're in some order, but I'm not telling you what order.
# You just have to make a guess, and I'll tell you
# of red, blue, green, and yellow, how many of the four
# you got in the right position.

# So a simplified version of this game.
# You might make a guess, like red, blue, green, yellow.
# And I would tell you something like, two of those four
# are in the correct position, but the other two are not.

# Then you could reasonably make a guess and say, all right, let's try this.
# Blue, red, green, yellow.
# Try switching two of them around.
# And this time maybe I tell you, you know what, none of those
# are in the correct position.

colors = ["red", "blue", "green", "yellow"]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

# Each color has a position.
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ))

# Only one position per color.
for color in colors:
    for i in range(4):
        for j in range(4):
            if i != j:
                knowledge.add(Implication(
                    Symbol(f"{color}{i}"), Not(Symbol(f"{color}{j}"))
                ))

# Only one color per position.
for i in range(4):
    for c1 in colors:
        for c2 in colors:
            if c1 != c2:
                knowledge.add(Implication(
                    Symbol(f"{c1}{i}"), Not(Symbol(f"{c2}{i}"))
                ))

knowledge.add(Or(
    And(Symbol("red0"), Symbol("blue1"), Not(Symbol("green2")), Not(Symbol("yellow3"))),
    And(Symbol("red0"), Symbol("green2"), Not(Symbol("blue1")), Not(Symbol("yellow3"))),
    And(Symbol("red0"), Symbol("yellow3"), Not(Symbol("blue1")), Not(Symbol("green2"))),
    And(Symbol("blue1"), Symbol("green2"), Not(Symbol("red0")), Not(Symbol("yellow3"))),
    And(Symbol("blue1"), Symbol("yellow3"), Not(Symbol("red0")), Not(Symbol("green2"))),
    And(Symbol("green2"), Symbol("yellow3"), Not(Symbol("red0")), Not(Symbol("blue1")))
))

knowledge.add(And(
    Not(Symbol("blue0")),
    Not(Symbol("red1")),
    Not(Symbol("green2")),
    Not(Symbol("yellow3"))
))

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)

# But as the number of variables increases,
# model checking becomes less and less good of a way of trying
# to solve these sorts of problems.
# So while it might have been OK for something like Mastermind
# to conclude that this is, indeed, the correct sequence,
# where all four are in the correct position, what we'd like to do
# is come up with some better ways to be able to make inferences, rather
# than just enumerate all of the possibilities.
# And to do so, what we'll transition to next is the idea of inference rules.
# Some sort of rules that we can apply to take knowledge that already exists
# and translate it into new forms of knowledge.