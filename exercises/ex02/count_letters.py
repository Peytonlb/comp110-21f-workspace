"""Counting letters in a string."""
__author__ = "730309987"
letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
index = 0
count = 0
while (count < len(word)):
    if(word[count] == letter):
        index = index + 1
    count = count + 1
print("Count:",index)