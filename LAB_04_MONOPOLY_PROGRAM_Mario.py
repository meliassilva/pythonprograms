# 1. Name:
#      Mario da Silva Filho
# 2. Assignment Name:
#      Lab 04: Monopoly
# 3. Assignment Description:
#      Prompt the user for some information and answer the  if he is able to put or not an hotel
# 4. What was the hardest part? Be as specific as possible.
#      Not very well I think I could put all in function but at least I got work
# 5. How long did it take for you to complete the assignment?
#      8 hours

import sys

# You cannot purchase a hotel until you own all the properties of a given color group.
# Do you own all the green properties? (y/n)
green_properties = input("Do you own all the green properties? (y/n) ")
if green_properties == ("n"):
    print("You cannot purchase a hotel until you own all the properties of a given color group.")
    sys.exit(0)
else:
    pass


#What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel)
pacific_question = int(
    input("What is on Pacific Avenue (0:nothing, 1:one house, ... 5:a hotel) "))
if pacific_question == 0:
    number_houses_pacific = 0
    need_houses_pacific = 4
    hotel_pacific = 0
    hotel_need_pacific = 1
    pass
if pacific_question == 1:
    number_houses_pacific = 1
    need_houses_pacific = 3
    hotel_pacific = 0
    hotel_need_pacific = 1
    pass
if pacific_question == 2:
    number_houses_pacific = 2
    need_houses_pacific = 2
    hotel_pacific = 0
    hotel_need_pacific = 1
    pass
if pacific_question == 3:
    number_houses_pacific = 3
    need_houses_pacific = 1
    hotel_pacific = 0
    hotel_need_pacific = 1
    pass
if pacific_question == 4:
    number_houses_pacific = 4
    need_houses_pacific = 0
    hotel_pacific = 0
    hotel_need_pacific = 1
    pass
if pacific_question == 5:
    need_houses_pacific = 0
    hotel_pacific = 1
    hotel_need_pacific = 0
    print(" You cannot purchase a hotel if the property already has one.")
    pass

# What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel)
northcarolina_question = int(input(
    "What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
if northcarolina_question == 0:
    number_houses_north = 0
    need_houses_north = 4
    hotel_north =0
    hotel_need_north = 1
    pass
if northcarolina_question == 1:
    number_houses_north = 1
    need_houses_north = 3
    hotel_north = 0
    hotel_need_north = 1
    pass
if northcarolina_question == 2:
    number_houses_north = 2
    need_houses_north = 2
    hotel_north = 0
    hotel_need_north = 1
    pass
if northcarolina_question == 3:
    number_houses_north = 3
    need_houses_north = 1
    hotel_north = 0
    hotel_need_north = 1
    pass
if northcarolina_question == 4:
    number_houses_north = 4
    need_houses_north = 0
    hotel_north = 0
    hotel_need_north = 1
    pass
if northcarolina_question == 5:
    need_houses_north = 0
    hotel_north = 1
    hotel_need_north = 0
    print(" You cannot purchase a hotel if the property already has one.")
    pass


#What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel)
pennsylvania_question = int(
    input("What is on Pennsylvania Avenue?(0:nothing, 1:one house, ... 5:a hotel) "))
if pennsylvania_question == 0:
    number_houses_pennsylvania = 0
    need_houses_penn = 4
    hotel_penn = 0
    hotel_need_peen =1
    pass
if pennsylvania_question == 1:
    number_houses_pennsylvania = 1
    need_houses_penn = 3
    hotel_penn = 0
    hotel_need_peen = 1
    pass
if pennsylvania_question == 2:
    number_houses_pennsylvania = 2
    need_houses_penn = 2
    hotel_penn = 0
    hotel_need_peen = 1
    pass
if pennsylvania_question == 3:
    number_houses_pennsylvania = 3
    need_houses_penn = 1
    hotel_penn = 0
    hotel_need_peen = 1
    pass
if pennsylvania_question == 4:
    number_houses_pennsylvania = 4
    need_houses_penn = 0
    hotel_penn = 0
    hotel_need_peen = 1
    pass
if pennsylvania_question == 5:
    need_houses_penn = 0
    hotel_penn = 1
    hotel_need_peen = 0
    print(" You cannot purchase a hotel if the property already has one.")
    pass


#How many houses are there to purchase?
houses_qty = int(input("How many houses are there to purchase? "))
#How many hotels are there to purchase?
hotels_qty = int(input("How many hotels are there to purchase? "))


availability = houses_qty - (need_houses_north + need_houses_pacific + need_houses_penn)
cost_houses = (need_houses_north + need_houses_pacific +
               need_houses_penn) * 200
if availability < 0:
    print("Not enough houses available!You need ay least 4 houses in each green property and houses available for that.")
else:
    print(f"Add {need_houses_north} house(s) to North Carolina,")
    print(f"Add {need_houses_pacific} house(s) to Pacific,")
    print(f"Add {need_houses_penn} house(s) to Pennsylvania,")
    pass

availability_hotels = hotels_qty - (hotel_pacific + hotel_penn + hotel_north)
cost_hotel = (hotel_need_north + hotel_need_peen + hotel_need_pacific) * 200
if availability_hotels <  0:
    print("There are not enough hotels available for purchase at this time.")
    sys.exit(0)
if availability_hotels > 0 and hotel_north == 0 and hotel_pacific == 0 and hotel_penn == 0:
    print("Put 1 hotel on Pacific, 1 hotel on North Carolina, and 1 hotel on Pennsylvania.")
    pass

#How much cash do you have to spend?
hand_cash = int(input("How much cash do you have to spend? "))
total_price  = (cost_houses + cost_hotel)
print(f"This will cost ${total_price}.")

if hand_cash < total_price :
    print("You do not have sufficient funds to purchase a hotel at this time.")


