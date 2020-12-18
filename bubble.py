# Python program for Bubble Sort

a = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element of List1 : " %i))
    a.append(value)

for i in range(number -1):
    for j in range(number - i - 1):
        if(a[j] > a[j + 1]):
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print("The Sorted List in Ascending Order : ", a)


def bubble_sort(our_list):
    # We want to stop passing through the list
    # as soon as we pass through without swapping any elements
    has_swapped = True

    while (has_swapped):
        has_swapped = False
        for i in range(len(our_list) - 1):
            if our_list[i] > our_list[i + 1]:
                # Swap
                our_list[i], our_list[i + 1] = our_list[i + 1], our_list[i]
                has_swapped = True