# class Node:
# def __init__(self, value, left=None, right=None):
#     self.left = left
#     self.right = right
#     self.value = value
#     self.count = 1

# def add(self, value):
#     if self.value == value:
#         self.count += 1
#     elif value < self.value:
#         if self.left is None:
#             self.left = Node(value)
#         else:
#             self.left.add(value)
#     else:
#         if self.right is None:
#             self.right = Node(value)
#         else:
#             self.right.add(value)

# def printTree(self):
#     if self.left is not None:
#         self.left.printTree()
#     print(str(self.value) + " " + str(self.count))
#     if self.right is not None:
#         self.right.printTree()


# def processFileContent(file):
#     words = []
#     for line in file:
#         unprocessedWords = re.split(" ", line)

#     for word in unprocessedWords:
#         word = word.lower()
#         if word.isalpha():
#             words.append(word)

# return words

# def processFile():
#     file = open("text.txt", "r")
#     words = processFileContent(file)
#     file.close()
#     return words


# def createTree(words):
#     if len(words) > 0:
#         tree = Node(words[0])
#         for word in words:
#             tree.add(word)
#         return tree
#     else:
#         return None

# def main():
#     words = processFile()
#     tree = createTree(words)
#     tree.printTree()





# from difflib import get_close_matches
# def search(tree, word):
#     node = tree
#     depth = 0
#     count = 0
#     while True:
#         print(node.value)
#         depth += 1
#         if node.value == word:
#             count = node.count
#             break
#         elif word < node.value:
#             node = node.left
#         elif word > node.value:
#             node = node.right

#     return depth, count

# def main():
#     print(search(tree, "a"))


# wordCheck = raw_input(
#     "please enter the word you would like to check the spelling of: ")
# with open("words.txt", "r") as f:
#     found = False
#     for line in f:
#         if line.strip() == wordCheck:
#             print('That is the correct spelling for ' + wordCheck)
#             found = True
#             break
#     if not found:
#         print(wordCheck + " is not in our dictionary")


# from difflib import get_close_matches

# with open('/usr/share/dict/words') as fin:
#     words = set(line.strip().lower() for line in fin)

# testword = 'hlelo'
# matches = get_close_matches(testword, words, n=5)
# if testword == matches[0]:
#     print 'okay'
# else:
#     print 'Not sure about:', testword
#     print 'options:', ', '.join(matches)

# #Not sure about: hlelo
# #options: helot, hello, leo, hollow, hillel



# from benchmark import load_names  # Sample code to download
# import random
# wordCheck = input(
#     "Please enter the word you would like to check the spelling of: ")

# with open('words.txt', 'r') as f:
#     for line in f:
#         if wordCheck in line.split():
#             print('That is the correct spelling for ' + wordCheck)
#             break
#     else:
#         print(wordCheck + " is not in our dictionary")


# # Python program to read
# # file word by word

# # opening the text file
# with open('GFG.txt', 'r') as file:

#     # reading each line
#     for line in file:

#         # reading each word
#         for word in line.split():

#             # displaying the words
#             print(word)


# # Return a list of names of some file
# def load_names(path):
#     with open(path) as text_file:
#         return text_file.read().splitlines()


# names = load_names('names.txt')
# sorted_names = load_names('sorted_names.txt')


# def find(elements, value):
#     while True:
#         random_element = random.choice(elements)
#         if random_element == value:
#             return random_element


# def find_index(elements, value):
#     for index, element in enumerate(elements):
#         if element == value:
#             return index


from benchmark import load_names  # Sample code to download
names = load_names('names.txt')
index_by_name = {
    name: index for index, name in enumerate(names)
    }

import math
def find_index(elements, value):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        if math.isclose(elements[middle], value):
            return middle

        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > value:
            right = middle - 1
