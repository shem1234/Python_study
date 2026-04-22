if 20> 50:
    print("20 is greater")
else:
    print("20 is less")

# check if someone is eligible to vote
age = 10

if age >= 18:
    print("Eligible to vote")
else: 
    print("Not eligible to vote")

# check if temperature is greater than 30 print too hot,
# if temperature is above 15 and less than 30 print normal
#  temperature otherwise too cold
temp = 10
if temp > 30:
    print("Too hot")
elif temp > 15 and temp <= 30:
        print("Normal")
else:
    print("Too cold")

# grading of marks
marks = 50

if marks >= 80:
        print("Grade A")
elif marks >=70 and marks < 80:
    print("Grade B")
elif marks >=60 and marks < 70:
    print("Grade C")
elif marks >=50 and marks < 60:
    print("Grade D")
else:
    print("Failed")
