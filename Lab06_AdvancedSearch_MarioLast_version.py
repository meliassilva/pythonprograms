# 1. Name:
#      Mario Elias da Silva Filho
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program are supposed to test an advanced search algorithm
# 4. Algorithmic Efficiency
#      The algorithm efficiency is O(log n), is little slow in the beggining but with a lot of of data in the array the speed is the same
#      I use the steps count and the datetime to calculate speed and how much interactions they have to find the thing, and
#      in the countries file they took just 8 steps max to find the name.
# 5. What was the hardest part? Be as specific as possible.
#      The while loops to grab the empty file
# 6. How long did it take for you to complete the assignment?
#      6 hours

import os.path
import json
from datetime import datetime


def read_data(filename):
    try:
        with open(filename) as file:
            js_dict = json.load(file)
            return js_dict['array']
    except IOError:
        print("This file doesn't exist.")
        return -1


def advanced_search(array, element):
    start = datetime.now()
    first_member = 0
    last_member = len(array)
    step = 0
    while first_member <= last_member:
        step += 1
        mid = (first_member + last_member) // 2
        if element == array[mid]:
            return mid, datetime.now() - start
        if array[mid] < element:
            first_member = mid + 1
        else:
           last_member = mid - 1
    return -1, datetime.now() - start



def main():
    filename = "mario"
    while filename != 'q':
        filename = str(input("Please input the filename or type q to quit the program: "))
        if filename == 'q' or filename == 'Q':
            # quit the program
            break
        else:
            data = read_data(filename)
            data.sort()
            if data == -1:
                pass
            if len(data) == 0:
                # empty file situation
                print("The file is empty!")
            else:
                # do the work
                word = input("What name are we looking for? ")
                result, time = advanced_search(data, word)
                if result != -1:
                    print("We found {} in {}. Performance: {}".format(word, filename, time))
                else:
                    print("{} is not in {}. Performance: {}".format(word, filename, time))
                print()



if __name__ == "__main__":
    main()
