from logic import *

rain = Symbol("rain") # It is raining
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

# STEP[ 0 ] - Create the symbols
# sentence = And(rain, hagrid)
# sentence = Or(rain, hagrid)
# print(sentence.formula())
# print(model_check(sentence, rain))


# STEP[ 1 ] - Create the knowledge base
# where we talked about trying to figure out who Harry visited,
# and trying to figure out if it's raining or if it's not raining.

# 1. if is not raining, then Harry visited Hagrid
# knowledge = Implication(Not(rain), hagrid)

# 2. Harry visited either Hagrid or Dumbledore
# knowledge = Or(hagrid, dumbledore)

# 3. Harry did not visit both Hagrid and Dumbledore
# knowledge = Not(And(hagrid, dumbledore))

# 4. Harry visited Dumbledore
# knowledge = dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(knowledge.formula())
# print(model_check(knowledge, rain))

# STEP[ 2 ] - Check if the knowledge base is consistent
# base on that information, do I know if it's raining or not?
# is the knowledge true and is the query true?
print(model_check(knowledge, rain))

# take a problem
# and figure out what propositional symbols to use in order
# to encode that idea, or how to represent it logically
# is known as knowledge engineering.
# That software engineers and AI engineers will take a problem
# and try and figure out how to distill it down into knowledge
# that is representable by a computer.

