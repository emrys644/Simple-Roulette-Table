import random
import time
from random import randint
winning_number = random.randint(0,36)
print("How much would you like to bet?")
money = int(input())
print("Your bet:",money)
print("red, green or black?")
print("red = 2x")
print("black = 2x")
print("green = 35x")
guess=input().lower()
if winning_number == 0:
    winning_color = "green"
elif winning_number % 2 == 0:
    winning_color = "black"
else:
    winning_color = "red"
print("Spinning...")
time.sleep(1)
print("Spun!")
print("So lets see.. Did you win??")
time.sleep(2)
if guess == winning_color:
    print("You win! Well done!")
    if guess == "green":
        print("You have won £",money * 35,"!")
    elif guess == "red" or guess == "black":
        print("You have won £",money * 2,"!")
else:
    print("Oh no! You lost! You could always try again!")
print("The color was" ,winning_color,".")

