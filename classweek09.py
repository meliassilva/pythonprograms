import random

def main():
    numberList = []  # create an empty list, to add 100 random ints to
    for i in range(100):
        numberList.append(random.randint(1,1000))  # add a random int

    # now, numberList has 100 random numbers in it

    # keep track of how many odd numbers
    oddCount = 0

    # loop through numberList
    for number in numberList:
        if number%2 == 1:  # number is odd
            oddCount += 1

    evenCount = 100 - oddCount  # if a number is not odd, it is not even

    print("There are", oddCount, "odd numbers, and", evenCount, "even numbers")


import random

NUMBER_LIST = [random.randint(0,1000)]
even = 0;
odd = 0;
for numbers in range(100):
    if (numbers%2 == 1):
        odd = odd+1
    if (numbers%2 == 0):
        even = even+1
print('number of evens is: ',even)
print('number of odds is: ',odd)




import random
NUMBER_LIST = []
evens = 0
odds = 0
i = 0
while i < 100:
    number = random.randint(0, 1000)
    NUMBER_LIST.append(number)
    if number % 2 == 0:
        evens += 1
    else:
        odds += 1
    i += 1
print("The numbers were: " + str(NUMBER_LIST))
print("The number of even numbers is: " + evens)
print("The number of odd numbers is: " + odds)

only_odd = [num for num in list1 if num % 2 == 1]
odd_count = len(only_odd)

print("Even numbers in the list: ", len(list1) - odd_count)
print("Odd numbers in the list: ", odd_count)


position = input("Whats your position in the last race?")
points_position = [500, 400, 325, 275, 225, 175, 150, 125, 100, 85, 70, 60, 50, 40]

