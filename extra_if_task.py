# Create a new file extra_if_task.py
# 1.
# Write a program that checks login credentials:
# "Access granted" if email = "admin@gmail.com" and password = "Admin@123"
# "Wrong password" if email is correct but password is wrong
# "Email not found" otherwise
email = input("Enter the email: ")
password = input("Enter the password: ")

emailc = "admin@gmail.com"
passwordc = "Admin@123"

if email == emailc and password == passwordc:
    print("Access granted")
elif email != emailc:
    print("Email not found")
else:
    print("Wrong password")

# 2.
# Create a program that validates an email:
# "Invalid email" if it does not contain "@" or "."
# "Gmail account" if it ends with "@gmail.com"
# "Other email provider" otherwise
email = input("Enter your email: ")

if email.find("@") == -1 or email.find(".") == -1:
    print("Invalid email")
elif email.endswith("@gmail.com"):
    print("Gmail account")
else:
    print("Other email provider")

# or
if "@" not in email or "." not in email:
    print("Invalid email")
elif email.endswith("@gmail.com"):
    print("Gmail account")
else:
    print("Other email provider")

# 3.
# Write a program that checks password strength:
# "Weak" if length < 6
# "Moderate" if length 6–10 and contains at least one digit
# "Strong" if length > 10 and contains both digits and uppercase letters
password = input("Enter the password: ")

if len(password) < 6:
    print("Weak")
elif len(password) >=6 and len(password) <= 10 and password.isalnum():
    print("Moderate")
elif len(password) > 10 and password.isalnum() and password.isupper():
    print("Srong")

# 4.
# Write a program that checks a password:
# "Invalid" if it does not start with a capital letter
# "Invalid" if it does not end with a number
# "Valid password" otherwise
password = input("Enter the password: ")

if password[0].isupper() and password[-1].isdigit():
    print("Valid")
else:
    print("Invalid")

# 5.
# Write a program that takes a number and checks:
# "Fizz" if divisible by 3
# "Buzz" if divisible by 5
# "FizzBuzz" if divisible by both
# Otherwise print the number
num = int(input("Enter the number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num% 5 == 0:
    print("Buzz")
else:
    print(num)

# 6.
# Create a program that takes a score and prints a grade:
# A (≥ 80)
# B (70–79)
# C (60–69)
# D (50–59)
# F (< 50)

# 7.
# Create a program that takes two numbers and prints:
# "Equal" if same
# "First is greater"
# "Second is greater"

# 8.
# Write a program that takes a day number (1–7) and prints:
# Weekday (1–5)
# Weekend (6–7)
# Invalid input otherwise

# 9.
# Create a program that takes a temperature and prints:
# "Freezing" if ≤ 0
# "Cold" if 1–15
# "Warm" if 16–30
# "Hot" if > 30

# 10.
# Create a program that takes a year and prints:
# "Leap year" if divisible by 4
# "Century year" if divisible by 100
# "Common year" otherwise
year = int(input("Enter the year: "))

if (year%100!=0 or year%400==0) and year%4==0:
    print("Leap year")
    
