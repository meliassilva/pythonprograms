# 1. Name:
#    -Mario Elias da Silva Filho-
# 2. Assignment Name:
#    Lab 01: Python Review
# 3. Assignment Description:
#    -This program is a game of guessing, just for entertainment-
# 4. What was the hardest part? Be as specific as possible.
#    The concatenation was a little trick for me -
# 5. How long did it take for you to complete the assignment?
#    -2 hours-

import random
import math


# Game introduction
print('Welcome to the Guessing Game')

# Prompt the user for how difficult the game will be. Ask for an integer
value_max = int(input('Please enter the max value: '))

# Generate a random number between 1 and the chosen value
random = int(random.randint(1, value_max))

# Give the user instructions as to what he or she will be doing
print('Now lets go play Guessing Game')
print('You have 5 attempts')

# Initialize the sentinal and the array of guesses
guess = (0);
list = [];

# Play the guessing game
while guess != random and len(list) <= 4:

    # Prompt the user for a number
    guess = int(input('Please enter your guess: '))
    # Store the number in an array so it can be displayed later
    list.append(guess)
    # Make a decision: was the guess too high, too low, or just right
    if (guess == random):
        print ('Awesome you Hit!')
    elif (guess < random):
        print ('Your guess is too low')
    else:
        print ('Your guess is too high')

# Give the user a report: How many guesses and what the guesses where
right_number = 'This is the ramdom number:{}'
print (right_number.format(random))
report = 'These are the numbers you tried:{}'
print (report.format(list))
attempts = 'You made it in {} attempts'
print (attempts.format(len(list)))
