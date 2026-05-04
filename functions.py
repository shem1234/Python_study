def hello():
    print("Hello")

hello()

# calculate the ares od a trianbgle

def triangle_area():
    base = 10
    height = 20
    area = 0.5 * base * height
    print(area)

triangle_area()

# create a function that calculats the area of a circle

def circle_area():
    radius = 10
    area = 3.14 * radius** 2
    print(area)

circle_area()

# parameters and arguments
def hello(name):
    print(f"Hello {name}")

hello("alex")

# create a function that calculates the area of a rectangle

def rectangle_area(length,height):
    area = length * height
    print(area)

rectangle_area(10,20)
rectangle_area(30,40)

# return
def hello(name):
    return f"Hello {name}"

name = hello("alex")
print(name)

# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display
#   either “odd” or “even” to the user. 
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
# Once you learn functions,revisit this and write this code inside a function.
number = int(input("Enter a number: "))

def even(number):
    if number % 2 == 0 and number % 4 != 0:
        return "even"
    elif number % 4 == 0:
        return "divisible by 4"
    else:
        return "odd"
 
res = even(number)
print(res)
