"""
File: 05_Prove_Assignment_Mario.py
Author: Brother Burton
Assignment: 005_Prove_Assignment_Mario _ Adventure Game
Purpose: Learning how to learn with different variable types and make
some calculation.
"""


def play():
    user_play = str(input("Do you want play? (yes or no) "))
    while user_play != "yes" or user_play != "no":
        return 1
    if user_play.lower == "yes":
        print("lets play!!!!")
        return 0
    if user_play.lower == "no":
        print("Ok, thank you for your time.")
        return quit()



def main():
    print("Welcome to the adventure Game")
    print("This is a game of choices, if you do the right choices you will see the final of the story")
    play()
    print("You enter yes")


if __name__ == "__main__":
    main()
