# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.
student_marks = int(input("Enter student marks: "))

if student_marks >=0 and student_marks <= 100:
    if student_marks > 79:
        grade = "A"
    elif student_marks >= 60 and student_marks <= 79:
        grade = "B"
    elif student_marks > 49 and student_marks <= 59:
        grade = "C"
    elif student_marks >= 40 and student_marks <= 49:
        grade = "D"
    else:
        grade = "E"
else:
    grade = "Invalid marks. Please enter a mark between 0 and 100"

print(grade)

# with funcion
def find_grade(marks):
    if marks >=0 and marks <= 100:
        if student_marks > 79:
            return "A"
        elif marks >= 60 and marks <= 79:
            return "B"
        elif marks > 49 and marks <= 59:
            return "C"
        elif marks >= 40 and marks <= 49:
            return "D"
        else:
            return "E"
    else:
        return "Invalid marks. Please enter a mark between 0 and 100"

student_marks = int(input("Enter student marks: "))
find_grade(student_marks)
print(find_grade(student_marks))

# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit 
# in every array/list.
# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
# Once you learn functions,revisit this and write this code inside a function.
prods = [["omo","30kshs",300],["milk","50kshs",200],["bread","45kshs",359],["coffee","5kshs",79]]

total_stock = 0

for i in prods:
    total_stock = total_stock + int(i[-1])

print(total_stock)

# with function
def calc_total_stock(my_list):
    total_stock = 0

    for i in my_list:
        total_stock = total_stock + int(i[-1])
    
    return total_stock

prods = [["omo","30kshs",300],["milk","50kshs",200],["bread","45kshs",359],["coffee","5kshs",79]]
stock1=(calc_total_stock(prods))
print(stock1)



