"""Repeating a beat in a loop."""
__author__ = "730309987"
beat: str = input("What beat do you want to repeat? ")
times: int = 0
maximum: int = int(input("How many times do you want to repeat it? "))
while times < maximum:
    print(beat) 
    times = times + 1 
if maximum < 1: 
    print("No beat...")