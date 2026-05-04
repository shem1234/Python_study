# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
# Once you learn functions,revisit this and write this code inside a function.
base = int(input("Enter the base: "))
height = int(input("Enter the height: "))

print(f"The are of the triangle is {base*height/2}.")

# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display
#   either “odd” or “even” to the user. 
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
# Once you learn functions,revisit this and write this code inside a function.
number = int(input("Enter a number: "))

if number % 2 == 0:
    res = "even"
    if number % 4 == 0:
        res = "divisible by 4"
else:
    res = "odd"

print(res)

# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with
#  +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.
phone = input("Enter phone number: ")
print(phone[0:4])

if phone[0:4] == "+254":
    if len(phone) == 13 and phone[1:14].isdigit():
        res = phone
    else:
        res = "Invalid phone number. Please reenter the phone numner"
elif phone[0:2] == "07" or phone[0:2] == "01":
    if len(phone) == 10 and phone[1:10].isdigit():
        res = "+254" + str(phone[1:10])
    else:
        res = "Invalid phone number. Please reenter the phone numner"
elif phone[0:1] == "7" or phone[0:1] == "1":
    if len(phone) == 9 and phone[1:9].isdigit():
        res = "+254" + str(phone[0:9])
    else:
        res = "Invalid phone number. Please reenter the phone numner"
else:
    res = "Invalid phone number. Please reenter the phone numner"

print(res)

# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# Once you learn functions,revisit this and write this code inside a function.
email = input("Enter your email: ")

if "@" in email and "." in email:
    res = "Valid email"
else:
    res = "invalid email"

print(res)

# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables.
#  Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3
    
print(largest)

# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against
#  “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.
counter = 3
i = 0

while i < counter:
    user = input("Please enter your password: ")
    if user == "admin@123":
        print("Access granted")
        break
    else:
        i = i + 1
        if i == counter:
            print("Account blocked")
        else:
            print("Wrong password. Please try again")

# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.
mark = 0

invalid = 0
i = 0
while i < 5 and invalid < 5:
    marks1 = int(input("Enter the first marks: "))
    if marks1 >= 0 and marks1 <= 100:
        mark = mark + marks1
        i = 6
        invalid = 0
    else:
        print("Invalid marks. Please enter a mark between 0 and 100")
        i = i + 1
        invalid = i

while i < 11 and invalid < 5:
    marks2 = int(input("Enter the second marks: "))
    if marks2 >= 0 and marks2 <= 100:
        mark = mark + marks2
        i = 12
        invalid = 0
    else:
        print("Invalid marks. Please enter a mark between 0 and 100")
        i = i + 1
        invalid = i

while i <= 17 and invalid < 5:
    marks3 = int(input("Enter the third marks: "))
    if marks3 >= 0 and marks3 <= 100:
        mark = mark + marks3
        i = 18
        invalid = 0
    else:
        print("Invalid marks. Please enter a mark between 0 and 100")
        i = i + 1
        invalid = i

if invalid != 0:
    print("You have entered too many invalid marks. Process terminated")
else:
    average = mark/3

    if average > 79:
        grade = "Grade A"
    elif average >= 60 and average <= 79:
        grade = "Grade B"
    elif average >= 49 and average <= 59:
        grade = "Grade C"
    elif average >= 40 and average <= 49:
        grade = "Grade D"
    else:
        grade = "Grade E"
    
    print(grade)

# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for
#  every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should
#  print: “License suspended”.
# Once you learn functions,revisit this and write this code inside a function.
speed = int(input("Enter the car speed: "))

if speed <= 70:
    res = "Ok"
elif speed > 70 and speed <= 75:
    res = "Points: 1"
elif speed > 75 and speed <= 80:
    res = "Points: 2"
elif speed > 80 and speed <= 85:
    res = "Points: 3"    
elif speed > 85 and speed <= 90:
    res = "Points: 4"
elif speed > 90 and speed <= 95:
    res = "Points: 5"
elif speed > 95 and speed <= 100:
    res = "Points: 6"
elif speed > 100 and speed <= 105:
    res = "Points: 7"    
elif speed > 105 and speed <= 110:
    res = "Points: 8"
elif speed > 110 and speed <= 115:
    res = "Points: 9"
elif speed > 115 and speed <= 120:
    res = "Points: 10"
elif speed > 120 and speed <= 125:
    res = "Points: 11"    
elif speed > 125 and speed <= 130:
    res = "Points: 12"
else:
    res = "License suspended"

print(res)

# TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....
# Once you learn functions,revisit this and write this code inside a function.
number = int(input("Enter a number: "))

display = "*"
i = 0


while i < number:
    print(display)
    display = display + str("*")
    i = i + 1

# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit 
# in every array/list.
# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
# Once you learn functions,revisit this and write this code inside a function.
prods = [["omo","30kshs",300],["milk","50kshs",200],["bread","45kshs",359],["coffee","5kshs",79]]
stock = 0

for i in prods:
    stock = stock + i[2]

print(stock)

# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.datetime
# Once you learn functions,revisit this and write this code inside a function.
import datetime

# today's date
x = datetime.datetime.now()

print(x.year)
print(x.month)
print(x.day)

date_str = input("Enter date (YYYY-MM-DD): ")

# Step 2: convert string → datetime object
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")

# Step 3: extract parts
year = date_obj.year
month = date_obj.month
day = date_obj.day

print("Year:", year)
print("Month:", month)
print("Day:", day)

years = x.year - year
months = x.month - month
days = x.day - day

if months < 0:
    years = years - 1
    months = months + 12

if days < 0:
    months = months - 1
    days = days + 30


print(f"Your age is {years} years, {months} month and {days} days.")

# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken as input from a user.
# Once you learn functions,revisit this and write this code inside a function.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
number4 = int(input("Enter the fourth number: "))

if number1 >= number2 and number1 >= number3 and number1 >= number4:
    largest = number1
elif number2 >= number1 and number2 >= number3 and number2 >= number4:
    largest = number2
elif number3 >= number1 and number3 >= number2 and number3 >= number4:
    largest = number3
else:
    largest = number4
    
print(largest)

# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and
#  password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”.
#  ONLY accept 3 tries after which it notifies you that you have been blocked.
# # Once you learn functions,revisit this and write this code inside a function.
i = 0

while i < 3:
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    if email == str("admin@mail.com") and password == str("Admin@123"):
        print("Login is Successful")
        break
    else:
        print("Invalid username or password")
        i = i + 1

if i == 4:
    print("Account blocked")

# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise
#  display an error “invalid character entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.
i = 0

while i < 3:
    number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")

    try:
        num1 = float(number1)
        num2 = float(number2)
    except:
        print("invalid character entered")
        i = i + 1
    else:
        sum = num1 + num2
        print(sum)
        break


