"""
File: 10_Prove_ListCartAssignment_Mario.py
Author: Mario Elias da Silva Filho
Assignment: 10 Prove
Purpose: Learning how to make loops, while and for.

"""
import sys

print("Welcome to the Shopping Cart Program!")

action = ""
shooping_list = []
price_list = []
sum_items = 0

while action != "5":

    print("Please select one of the following:  ")
    print("1.Add a new item")
    print("2.Display the contents of the shopping cart")
    print("3.Remove an item")
    print("4.Compute the total")
    print("5.Quit")

    action = input("Please select one of the following:  \n")

    if action == "1":
        shopping_item = input("What item would you like to add?")
        price = float(input(f"What is the price of {shopping_item} ? "))
        shooping_list.append(shopping_item)
        price_list.append(price)
        print(f"{shopping_item} has been added to the cart.\n")

    elif action == "2":
        print("The contents of your cart are: ")
        for i in range(len(shooping_list)):
            item = shooping_list[i]
            price = price_list[i]
            print(f"{i+1}. {item} -- {price} ")

    elif action == "3":
        removal = int(input("Which item would you like to remove?"))
        shooping_list.pop(removal - 1)
        price_list.pop(removal -1)
        print("item removed \n")

    elif action == "4":
        for i in range(0, len(price_list)):
            sum_items = sum_items + price_list[i];
        print(f"The total price of the items in the shopping cart is ${sum_items}")


    elif action == "5":
        print("Thank you. Goodbye.")
        exit(0)
