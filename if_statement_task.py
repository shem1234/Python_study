# 1. Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
num1 = 30
num2 = 20
num3 = 20

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num3:
    print(num2)
else:
    print(num3)

# 2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,
# if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp = 40

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

