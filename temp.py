mark = 0

i = 0
while i < 2:
    marks1 = int(input("Enter the first marks: "))
    if marks1 >= 0 and marks1 <= 100:
        mark = mark + marks1
        i = 10
    else:
        print("Invalid marks. Please enter a mark between 0 and 100")
        i = i + 1

if i == 10:
    i = 0

while i < 2:
    marks2 = int(input("Enter the second marks: "))
    if marks2 >= 0 and marks2 <= 100:
        mark = mark + marks2
        i = 10
    else:
        print("Invalid marks. Please enter a mark between 0 and 100")
        i = i + 1

if i == 10:
    i = 0

while i <= 2:
    marks3 = int(input("Enter the third marks: "))
    if marks3 >= 0 and marks3 <= 100:
        mark = mark + marks3
        i = 10
    else:
        print("Invalid marks. Please enter a mark between 0 and 100")
        i = i + 1

if i == 10:
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
else:
    print("You have entered too many invalid marks. Process terminated")


