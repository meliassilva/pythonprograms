"""
File: 03_Prove_Milestone_Mario.py
Author: Brother Burton
Assignment: 03 Prove: Milestone - Meal Price Calculator
Purpose: Learning how to work with a different variable types
"""
import math

# Ask the user for the following:
# The price of a child's meal(floating point)
child_meal_price = float(input("What is the price of a child's meal? "))

# The price of an adult's meal(floating point)
adult_meal_price = float(input("What is the price of an adult's meal? "))

# The number of children(integer)
children_qty = int(input("How many children are there? "))

# The number of adults(integer)
adults_qty = int(input("How many adults are there? "))

# The sales tax rate(floating point)
sales_tax_rate = float(input("What is the sales tax rate? "))

# Determine the meal's subtotal(before adding sales tax)
# by multiplying the number of children by the price of their meal,
total_children_meal = child_meal_price * children_qty

# and multiplying the number of adults by the price of their meal
total_adult_meal = adult_meal_price * adults_qty

# and adding those two values together.
subtotal =  total_adult_meal + total_children_meal

# Display the subtotal.
print("Subtotal $" , subtotal)

# Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.
sales_tax_total = (sales_tax_rate * subtotal) / 100
print("Sales Tax $" + str("%.2f" % sales_tax_total))

# Compute and display the total price of the meal by adding the subtotal and the sales tax.
total_price = sales_tax_total + subtotal
print("Total $" + str("%.2f" % total_price))

# Ask the user for the the payment amount(floating point)
payment_amount = float(input("What is the payment amount? "))

# Compute and display the change.
change = payment_amount - total_price
print("Change: $" + str("%.2f" % change))
