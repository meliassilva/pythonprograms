# 1. Name:
#      Mario Elias da Silva Filho
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:ci
#      Make the selection sort and measure the efficiency
# 4. What was the hardest part? Be as specific as possible.
#      My loop  figure out how to make the for in the sort function was a little trick
# 5. How long did it take for you to complete the assignment?
#      5 hours

import os.path
import json
from datetime import datetime


def assert_test(value):
    assert value == 1, "File does not Exists!"

    assert value == 2, "File is Empty!"

def read_data(filename):
    try:
        with open(filename) as file:
            js_dict = json.load(file)
            return js_dict['array']
    except IOError:
        assert_test(2)

def sort(data):
    start = datetime.now()
    i_pivot = len(data) - 1
    copy_data = data

    if len(data) == 0:
        assert_test(1)

    #Loop to organize and sort the data
    while i_pivot > 0:
        for i in range(i_pivot, 0, -1):
            for j in range(i):
                if data[j]>data[j+1]:
                    copy_data = data[j]
                    data[j] = data[j+1]
                    data[j+1] = copy_data
        return data, datetime.now() - start


def main():
    filename = "filename"
    filename = str(input("What is the name of the file? ")) #Prompt for file
    data = read_data(filename) #Call read_data function to store the file data into variable

    if len(data) == 1:
        print("\t" + str(data))
    else:
        sort_data = sort(data)
        print("The value in " + str(filename) + " are:")
        for x in sort_data:
            print("\t" + str(x))

if __name__ == "__main__":
    main()