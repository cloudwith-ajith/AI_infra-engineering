"""from random import choice

p = choice(["thala","thalapathy","STR"])
print(p)"""


"""
import random

number = random.randint(1,12)
print(number)"""

# this is using the shuffle()

"""
import random

cards = ["thala","thalapathy","STR"]
random.shuffle(cards)
for card in cards:
    print(card)

        """

import sys

if len(sys.argv) < 2:
    sys.exit("less argument ")
# elif len(sys.argv) > 2:
#     sys.exit("to many argument")
for i in sys.argv[1:]:
    print("hi", i)