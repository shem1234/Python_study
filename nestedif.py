1.# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive
age = int(input("Enter your age: "))


if age >= 18:
    license = input("Do you have a driver's license? Yes/No: ")
    if license == "Yes":
        print("You are eligible to drive.")
    else:
        print("You are not eligible to drive.")
else:
    print("You are too young to drive.")

2.# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."

score = int(input("Enter the credit score: "))
income = int(input("Enter the income: "))

if score > 700 and income > 50000:
    if income > 50000:
        print("Loan approved")
    else:
        print("Income requirement not met.")
else:
    print("Credit score too low.")

