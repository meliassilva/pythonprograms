# 1. Name:
#      Mario Elias da Silva Filho
# 2. Assignment Name:
#      Lab 12: Prime Numbers
# 3. Assignment Description:
#      Prompt the user for a number and display all the Prime Numbers between 2 and the given number
# 4. What was the hardest part? Be as specific as possible.
#      For me, anytime there is a double for loop my mind will get a bit messed up. But I got it to work
# 5. How long did it take for you to complete the assignment?
#      3 Hours. It is weird, but I felt like even if the assignments is getting a bit harder, my mind is
#      getting faster to figure the solution out.


count = 0
prime_numbers = []
n = 0
while n < 2:
    try:
        n = int(input("This program will find all the prime numbers at or below N. Select that N: "))
    except ValueError as ve:
        print("You are supposed to Select an Integer")

for i in range(2, n + 1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        prime_numbers.append(i)


print("The prime numbers at or below", n, "are:", prime_numbers)
