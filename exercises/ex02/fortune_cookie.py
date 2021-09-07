"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730309987"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
import random
print("Your fortune cookie says...")
fortune: int = (random.randint(1, 5))
if fortune == 1:
    print("Good fortune is coming your way.")
else:
    if fortune == 2:
        print("All things are difficult before they are easy.")
    else:
        if fortune == 3:
            print("Someone beautiful is coming into your life soon.")
        else:
            if fortune == 4:
                print("Laugh loud, long, and often.")
print("Now, go spread positive vibes!")