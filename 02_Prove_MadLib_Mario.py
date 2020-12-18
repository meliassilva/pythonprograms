# File: 02_Prove_MadLib_Mario.py
# Author: Mario da Silva Filho
# Assignment: 02 Prove: Assignment - Word Games
# Purpose: Prompt a user for things and display all together with a story and concatening everything.

# Introduction
print('Hello, how are you? Lets play MadLib Games')

name = input ('First I wanna know your name: ')
print('Welcome to the game ', name)
print('Lets start with some questions: ')

# questions for the public
adjective = input('Please enter an adjective: ')
noun = input('Please enter a noun: ')
noun_2 = input('Please enter another noun: ')
verb_1 = input('Please enter the first verb: ')
verb_2 = input('Please enter the second verb: ')
verb_3 = input('Please enter one more verb: ')
exclamation = input('Please enter an exclamation: ')

File

# Review
print("Your adjective is: ", adjective)
print("Your noun is: ", noun)
print("Your noun2 is: ", noun_2)
print("Your verb is: ", verb_1)
print("Your verb is: ", verb_2)
print("Your verb is: ", verb_3)
print("Your exclamation is : ", exclamation)

# Present the first story with the words input
story = 'The other day, I was really in trouble. It all started when I saw a very {} {} {} down the hallway. {} I yelled. But all I could think to do was to {} over and over. Miraculously, that caused it to stop, but not before it tried to {} right in front of my family.'
print('This is your first story: ')
print(story.format(adjective, noun, verb_1, exclamation, verb_2, verb_3))

# Present the second story with the words input
story_2 = 'We walk into the wood with {}. When we saw {} and we start to {} and {}, yelling {}. We try to figure out the way at home and we started to {} when we finally found {}. We running fast to {} and then we realize we woke up. And mom said: "Is just a dream my little one"'
print('This is the second story: ')
print(story_2.format(noun_2, noun, verb_2, verb_3, exclamation, verb_1, adjective, noun))
