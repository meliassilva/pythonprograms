# # Python program to demonstrate insert operation in binary search tree

# # A utility class that represents an individual node in a BST
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# # A utility function to insert a new node with the given key


# def insert(root, key):
#     if root is None:
#         return Node(key)
#     else:
#         if root.val == key:
#             return root
#         elif root.val < key:
#             root.right = insert(root.right, key)
#         else:
#             root.left = insert(root.left, key)
#     return root

# # A utility function to do inorder tree traversal


# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.val)
#         inorder(root.right)


# # Driver program to test the above functions
# # Let us create the following BST
# #    50
# #  /     \
# # 30     70
# #  / \ / \
# # 20 40 60 80

# r = Node(50)
# r = insert(r, 30)
# r = insert(r, 20)
# r = insert(r, 40)
# r = insert(r, 70)
# r = insert(r, 60)
# r = insert(r, 80)

# # Print inoder traversal of the BST
# inorder(r)


# # A utility function to search a given key in BST
# def search(root, key):

#     # Base Cases: root is null or key is present at root
#     if root is None or root.val == key:
#         return root

#     # Key is greater than root's key
#     if root.val < key:
#         return search(root.right, key)
#     # Key is smaller than root's key
#     return search(root.left, key)


# def contains(elements, value):
#     def recursive(left, right):
#         if left <= right:
#             middle = (left + right) // 2
#             if elements[middle] == value:
#                 return True
#             if elements[middle] < value:
#                 return recursive(middle + 1, right)
#             elif elements[middle] > value:
#                 return recursive(left, middle - 1)
#         return False
#     return recursive(0, len(elements) - 1)


# # Python 3 program for recursive binary search.
# # Modifications needed for the older Python 2 are found in comments.

# # Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):

#     # Check base case
#     if high >= low:

#         mid = (high + low) // 2

#         # If element is present at the middle itself
#         if arr[mid] == x:
#             return mid

#         # If element is smaller than mid, then it can only
#         # be present in left subarray
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)

#         # Else the element can only be present in right subarray
#         else:
#             return binary_search(arr, mid + 1, high, x)

#     else:
#         # Element is not present in the array
#         return -1


# # Test array
# arr = [2, 3, 4, 10, 40]
# x = 10

# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)

# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")


# # Iterative Binary Search Function
# # It returns index of x in given array arr if present,
# # else returns -1
# def binary_search(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = 0

#     while low <= high:

#         mid = (high + low) // 2

#         # Check if x is present at mid
#         if arr[mid] < x:
#             low = mid + 1

#         # If x is greater, ignore left half
#         elif arr[mid] > x:
#             high = mid - 1

#         # If x is smaller, ignore right half
#         else:
#             return mid

#     # If we reach here, then the element was not present
#     return -1


# # Test array
# arr = [2, 3, 4, 10, 40]
# x = 10

# # Function call
# result = binary_search(arr, x)

# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")








#   // initially called with low = 0, high = N-1
#   BinarySearch(A[0..N-1], value, low, high) {
#       // invariants: value > A[i] for all i < low
#                      value < A[i] for all i > high
#       if (high < low)
#           return not_found // value would be inserted at index "low"
#       mid = (low + high) / 2
#       if (A[mid] > value)
#           return BinarySearch(A, value, low, mid-1)
#       else if (A[mid] < value)
#           return BinarySearch(A, value, mid+1, high)
#       else
#           return mid
#   }










#   BinarySearch(A[0..N-1], value) {
#       low = 0
#       high = N - 1
#       while (low <= high) {
#           // invariants: value > A[i] for all i < low
#                          value < A[i] for all i > high
#           mid = (low + high) / 2
#           if (A[mid] > value)
#               high = mid - 1
#           else if (A[mid] < value)
#               low = mid + 1
#           else
#               return mid
#       }
#       return not_found // value would be inserted at index "low"
#   }