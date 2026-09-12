import random
import time
from random import randint
winning_number = random.randint(0,36)
print("red, green or black?")
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
else:
    print("Oh no! You lost! You could always try again!")
    