# 1. Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)

# 2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,
# if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp = int(input("Enter the temperature: "))

if temp > 30:
    print("The temperature is too high")
elif temp > 15 and temp <= 30:
        print("Normal temperature")
else:
    print("Cold temperature")

# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x = 10
y = 99

if x >= 10 and x <=20 and y > 100:
    print("Conditions met")
else:
    print("Conditions not met")

# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is,
#  print "Access   granted", otherwise print "Access denied"
password = "secre123"

if password == "secret123":
    print("Access granted")
else:
    print("Access denied")

# Get 4 inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(num1)
elif num2 > num3 and num2 > num4:
    print(num2)
elif num3 > num4:
    print(num3)
else:
    print(num4)

# Create a program that checks a user's balance
# Insufficient funds if < 100
# moderate balannce if 100-1000
# High balance if > 1000
bal = int(input("Enter the bank balance: "))

if bal < 100:
    print("insufficient funds")
elif bal >= 100 and bal <= 1000:
    print("Moderate balance")
else:
    print("High balance")

# Write a program that checks:
# Small if number < 10
# Medium if 10-50
# Large if above 50
num = int(input("Enter the size: "))

if num < 10:
    print("Small")
elif num >=10 and num <= 50:
    print("Medium")
else:
    print("Large")

# Write a program that asks the user for email and password
# checks if the email is equal to "admin@gmail.com" and 
# password is equal to "admin123". if it is print Access granted
# otherwise print Access Denied
user = "admin@gmail.com"
password = "" \
""

user1 = input("Enter the user name: ")
password1 = input("Enter the password: ")

if user1 == user and password1 == password:
    print("Access")
else:
    print("Access Denied")

