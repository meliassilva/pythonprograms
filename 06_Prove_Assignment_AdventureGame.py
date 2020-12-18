"""
File: 06_Prove_Assignment_AdventureGame.py
Author: Mario Elias da Silva Filho
Assignment: 06 Prove: Assignment - Adventure Game
Purpose: Learning  to know how programs make decisions.
"""
print("Welcome to my game")
print("In a huge virus pandemic your friend invite you to go to a party")

while True:
    try:
        select = input("Do you go? select  # 1 or not select #2?> ")
        if select == ("1") or select == ("2"):
            break
    except ValueError:
        pass

if select == "1":
    print("Has a lot of people on the party are you using mask?")
    print("1. Yes")
    print("2. No")
    print("3. Just for a few time")

    while True:
        try:
            mask = input("> ")
            if mask == ("1") or mask == ("2") or mask == ("3"):
                break
        except ValueError:
            pass
    if mask == "1":
        print("Are you doing great, at least you are follow the rules.")
    elif mask == "2":
        print("Party is awesome. Few days latter you got sick. More few days you die")
    else:
        time = int(input("How much time do you the mask(in percentage between(0 - 100): "))
        if time >= 50:
            print("You follow the health instructions a good time, ")
            print("but you got sick, not die, but lost a lot of weight ")
            print("and lost all your assignments your fail in all your classes this semester")
        else:
            print("Party is awesome. Few days latter you got sick. More few days you die")


elif select == "2":
    print("You stay at home safe? What you do now")
    print("1. Cooking.")
    print("2. Watch a movie.")
    print("3. Do your homework")

    while True:
        try:
            home = input("> ")
            if home == ("1") or home == ("2") or home == ("3"):
                break
        except ValueError:
            pass

    if home == "1":
        print("You make an amazing Italian Spaghetti Good job!")
    elif home == "2":
        print("You watch the Lords of the Ring !!! It's a great movie!")
    else:
        print("You finish everything you need.")
        print("After few weeks you receive an A in all assignments !!!! GREAT WORK!!!")

else:
    print("You just fall sleep and forgot about party")
