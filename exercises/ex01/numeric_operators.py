"""Numeric Operators: 4 Specific Operators Computed, Given the 2 Values."""

__author__ = "730309987"

left_side: str = input("Left-hand side: ")
right_side: str = input("Right-hand side: ")
print(str(left_side) + " ** " + str(right_side) + " is " + str(int(left_side) ** int(right_side)))
print(str(left_side) + " / " + str(right_side) + " is " + str(int(left_side) / int(right_side)))
print(str(left_side) + " // " + str(right_side) + " is " + str(int(left_side) // int(right_side)))
print(str(left_side) + " % " + str(right_side) + " is " + str(int(left_side) % int(right_side)))