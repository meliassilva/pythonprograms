# 1. Name:
#      Mario Elias da Silva Filho
# 2. Assignment Name:
#      Lab 12: Prime Numbers
# 3. Assignment Description:
#      Prompt the user for a number and display all the Prime Numbers between 2 and the given number
# 4. What was the hardest part? Be as specific as possible.
#      For me, anytime there is a double for loop my mind will get a bit messed up. But I got it to work
# 5. How long did it take for you to complete the assignment?
#      Optimizing the things according to teacher solution.

from datetime import datetime

print ("This number will find the prime numbers between some number range:")

done = "N"
while (done.lower != "Y"):
    try:
        choice_number = int(input('Enter a number: '))
        assert choice_number > 0
    except AssertionError :
        print("Number is negative, Please insert a positive integer")

    prime_numbers = []
    first_number = 0
    start = datetime.now()

    if choice_number == 1:
        prime_numbers.append(1)

    for i in range(first_number, choice_number):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                prime_numbers.append(i)

    time_efficiency = datetime.now() - start
    print(time_efficiency)
    print(prime_numbers)

    done = input("Are you done? Y/N: ")

print("Thank you have agreat day")