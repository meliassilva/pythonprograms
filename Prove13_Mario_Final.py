"""
File: Prove13_Mario_Final.py
Author: Mario Elias da SIlva Filho
Assignment: Wind Chill Calculations
Purpose: practice functions
"""

wind_speed = [5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 60.0]

def compute_wind_chill(temp):
    wind_chill = 35.74 + 0.6215*t - 35.75* (v**0.16) + 0.4275 *t* (v**0.16)
    return wind_chill

def compute_temp_C (temp):
    temp_celsius = (temp * 9/5) + 32
    return temp_celsius


temp = float(input("What is the temperature ? "))
c_or_f = input("Fahrenheit or Celsius (F/C)? ")
if c_or_f.lower() == "f":
    t = temp
if c_or_f.lower() == "c":
    # The above code allows for input of Celsius temp without setting up a function.
    compute_temp_C (temp)
    temp_F = compute_temp_C (temp)
    t = temp_F


for v in wind_speed:
    compute_wind_chill (temp)
    wc = compute_wind_chill (temp)
    print (f"At temperature {t} F and wind speed of {v} mph, the windchill is: {wc:.2f} F")