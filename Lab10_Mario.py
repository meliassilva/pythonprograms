# 1. Name:
#      Mario Elias da Silva Filho
# 2. Assignment Name:
#      Lab 10: Fibonacci
# 3. Assignment Description:
#      Prompt for the  number n in position and return the Fibonacci
#      number on that position.
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part of this assignment was to find the right values to initiate
#      the program.
# 5. How long did it take for you to complete the assignment?
#      4 hours.
from datetime import datetime

position_n = int(input('Which Fibonacci number would you like to see? '))

loop_num = position_n + 2
f1 = 0
f2 = 1
count = 3
f3 = 0

start = datetime.now()
while count <= loop_num:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    count += 1

time_efficiency = datetime.now() - start
print(time_efficiency)
print(f"Fibonacci number {position_n} is {f3}")
