# GROUP 4
# Q1
# A school wants to stop students with pending balances from
#  sitting exams. Create a program that checks a student’s fee
#  balance. If the balance is greater than zero, deny access 
# to the exam card. Otherwise allow printing.

student = input("Enter the sudent name: ")
balance = float(input("Enter student fee balance: "))

if balance > 0:
    res = f"Hello {student}. Access denied. Balance should be less than 0"
else:
    res = f"Hello {student}. Access granted"

print(res)

# Q2
# A parking company wants to automate entry control. Build 
# a program that stores the total parking spaces and occupied 
# spaces, then calculates available slots. If the lot is full, 
# deny new entry.

total_space = int(input("Enter total parking spaces"))
occupied_spaces = int(input("Enter total occupied spaces"))
available_spaces = total_space - occupied_spaces

if available_spaces > 0:
    value = f"Entry allowed {available_spaces -1} spaces available"
else:
    value = f"Entry denied. Parking is full"

print(value)

# Q3
# A mobile network provider wants to warn customers when 
# internet bundles are low. Build a program that checks 
# remaining data in MB. If below 100MB, warn the user. 
# If zero, block browsing.

balance = int(input("Ener the remaining internet bundles balance: "))

if balance == 0:
    res = "Block user"
elif balance < 100:
    res = f"Warning. Your balance is {balance}"
else:
    res = f"Your balance is {balance}"

print(res)

# Q4
# A retail shop wants to identify wholesale customers. 
# Create a system that checks how many items a customer 
# has bought. If items are more than five, reward points 
# should be given.

items = int(input("Enter the items bought: "))

if items > 5:
    reward = int(items/5)
    res = f"You have bought {items} items. You have earned {reward} reward points"
else:
    res = f"You have bought {items} items. Purchase {5 - items} items to receive reward points"

print(res)
