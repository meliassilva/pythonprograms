# 1. Name:
#    -Mario Elias da Silva Filho-
# 2. Assignment Name:
#    Lab 02: Authentication
# 3. Assignment Description:
#    -Check username and password from a user-
# 4. What was the hardest part? Be as specific as possible.
#    - putting the data inside a dictionary, the syntax was a little trick to me-
# 5. How long did it take for you to complete the assignment?
#    -2 hours-

# Import json library to work with the json file
import json

# Open json file
f = open("Lab02.json", mode = 'r')

# Read the data from the file into a single string.
data = f.read()

# Convert the username and password components of the JSON object into two lists.
credentials = json.loads(data)
f.close()

# Prompt the user for password and username
username = input("Username: ")
password = input("Password: ")

# Compare with the list # Return Success or not
if username in credentials["username"] and password in credentials["password"]:
    print("You are authenticated!")
else:
    print("You are not authorized to use the system.")

