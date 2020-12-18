import json
import timeit

##get input
def prompt_filename():
    filename = input("Please enter the data file: ")
    return filename

##get input
def prompt_word():
    word = input("Please enter the word u looking for: ")
    return word


start = timeit.default_timer()


##read file
def read_binary_search(filename, word):
    file = open(filename)
    str = file.read().replace("\n", " ")
    line = str.split()
    file.close()
    if (binarySearch(line,word) != -1):
        print ("It's in the file")


def binarySearch(arr, x):
    l = 0
    r = len(arr)
    while (l <= r):
        m = l + ((r - l) // 2)

        res = (x == arr[m])

        # Check if x is present at mid
        if (res == 0):
            return m - 1

        # If x greater, ignore left half
        if (res > 0):
            l = m + 1

        # If x is smaller, ignore right half
        else:
            r = m - 1

    return -1

##main function to call other functions
def main():
    filename = prompt_filename()
    word = prompt_word()
    start = timeit.default_timer()
    read_binary_search(filename, word)
    stop = timeit.default_timer()
    print('Time: ', stop - start)

if __name__ == "__main__":
    main()
