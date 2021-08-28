"""Relational Operators: Testing 4 Specific Operators with 2 Inputs."""

__author__ = "730309987"

left_side: str = input("Left-hand side: ")
right_side: str = input("Right-hand side: ")
print(str(left_side) + " < " + str(right_side) + " is " + str(int(left_side) < int(right_side)))
print(str(left_side) + " >= " + str(right_side) + " is " + str(int(left_side) >= int(right_side)))
print(str(left_side) + " == " + str(right_side) + " is " + str(int(left_side) == int(right_side)))
print(str(left_side) + " != " + str(right_side) + " is " + str(int(left_side) != int(right_side)))