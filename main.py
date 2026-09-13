import random
import time
from random import randint
wallet = 100
print("Welcome to roulette!")

while True:
    
    
    winning_number = random.randint(0,36)
    print("How much would you like to bet?")
    print("You have", wallet, "in your account.")
    money = int(input())
    while money > wallet:
        print("Not enough funds!")
        print("You only have", wallet,".")
        money = int(input())
    print("Your bet:",money)
    wallet -= money
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
            wallet += money * 35
        elif guess == "red" or guess == "black":
            print("You have won £",money * 2,"!")
            wallet += money * 2
    else:
        print("Oh no! You lost! You could always try again! (unless money is 0)")
    print("The color was" ,winning_color,".")
    
    if wallet == 0:
        print("Sorry! You cant play anymore. Restart to get your money back!")
        break
    
    print("Would you like to spin again? (yes/no)")
    play_again = input().lower()
    
    
    
    if play_again == "no":
        print("Thanks for playing! Goodbye.")
        break
