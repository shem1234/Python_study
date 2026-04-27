# GROUP 7
# Q1
# A payroll company needs to calculate employee taxes using
#  different salary bands. Create a system that applies
#  different tax rates depending on salary level and displays
#  final pay.
salary = int(input("Enter the salary amount: "))

if salary > 32333:
    tax = (salary-32333) * 30/100 + 2400 + 2083.25
elif salary >= 24000 and salary <= 32333:
    tax = (salary-24000) * 25/100 + 2400
else:
    tax = salary * 10/100

print("Your salary is " + str(salary))
print("Tax: " + str(int(tax)))
print("Net pay: " + str(int(salary-tax)))

# Q2
# A university hostel manager wants to know whether rooms 
# are available. Create a program that checks room count and 
# rejects new applicants when no rooms remain.
rooms = 50

booking = int(input("Enter the rooms booking: "))

if booking > rooms:
    res = f"Only {rooms} rooms are available"
else:
    res = f"{booking} rooms booked. {rooms - booking} rooms available"

print(res)

# Q3
# An investor watches stock prices daily. Build a program that
#  sends alerts whenever a stock price drops below a chosen 
# buying target.

target = 100
price = int(input("Enter the stock price: "))

if price < target:
    res = f"Alert! The price is below target by {target-price}"
else:
    res = f"The price is above target by {price-target}"

print(res)

# Q4
# A ride-hailing company wants to manage customer expectations.
#  If no drivers are available nearby, inform the customer to 
# retry later.

driver = int(input("Insert the number of drivers available: "))

if driver > 0:
    res = "There is a driver available. Please wait."
else:
    res = "Unfortunately there is no driver available. Please try again later."


print(res)

