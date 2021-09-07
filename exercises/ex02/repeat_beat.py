"""Repeating a beat in a loop."""
__author__ = "730309987"
times: int = 0
beat: str = input("What beat do you want to repeat? ") 
maximum: int = int(input("How many times do you want to repeat it? "))
while times < maximum:
    repeat: str = (beat + " ") * (maximum -1)
    print(beat + " " + repeat) 
    break
if maximum < 1: 
    print("No beat...")