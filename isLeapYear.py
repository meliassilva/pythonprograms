# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))


# Python code to demonstrate the working of isleap()

# importing calendar module for calendar operations
import calendar
year = 2017

# calling isleap() method to verify
val = calendar.isleap(year)

# checking the condition is True or not
if val == True:

    # print 4th month of given leap year
    calendar.prmonth(year, 4, 2, 1)

# Returned False, year is not a leap
else:
    print("% s is not a leap year" % year)


# User enters the year
year = int(input("Enter Year: "))

# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


def LeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0)


def is_leap(year):
    return year % 4 == 0 and not (year % 100 == 0 and not year % 400 == 0)

year = int(input())

print(is_leap(year))
