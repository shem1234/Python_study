# Write a program that displays a numbers 1 to 50 inside a list.
numbers = list(range(1,50))

print(numbers)

# From 1 above display the ones divisible by 7 or 5 inside a list.
numbers = list(range(1,50))
display = []

for i in numbers:
    if i % 7 == 0 or i % 5 == 0:
        display.append(i)

print(display)

# Find sum and average of values in the range between 10 to 40.
numbers = list(range(10,41))
sum = 0
length = 0

for i in numbers:
    sum = sum + i
    length = length + 1

print(f"Sum is equal to {sum}.")
print(f"Average is equal to {sum/length}")

# Put in a list the first 10 odd numbers between 10 to 50. 
numbers = list(range(10,50))
display = []
counter = 0

for i in numbers:
    if i % 2 != 0:
        counter = counter + 1
        if counter <= 10:
            display.append(i)
        else:
            break

print(display)

# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
table = list(range(1,11))
number = int(input("Enter a number: "))

for i in table:
    print(f"{number} x {i} = {number*i}")

# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
numbers = list(range(1,51))
counter = 0

for i in numbers:
    if i % 2 == 0:
        counter = counter + 1

print(counter)

# ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
# Display the total quantity of the 3 above.
list1 = [ ("Jay", "20"), ("Mo", "30"), ("Mya", "32") ]
total = 0
number = 0

for i in list1:
    total = total + int(list1[number][1])
    number = number + 1

print(total)                         
