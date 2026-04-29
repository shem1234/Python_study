fruits = ["Mango","Orange","Banana"]

for i in fruits:
    print(i)

# # loop within the range
data = list(range(1,4))
print(list)

for x in data:
    print(x)

# display even numbers between 10 and 100
numbers = list(range(10,100))
even_numbers=[]

for i in numbers:
    if i%2==0:
        even_numbers.append(i)
        
print(even_numbers)

# display number divisible by 3 and 7 from numbers 1 to 100
numbers = list(range(1,100))
joint=[]

for i in numbers:
    if i % 3 == 0 and i % 7== 0:
        joint.append(i)

print(joint)

# enter PIN a maximum of 3 attempts, then block the account.
tries = 3
attempts = 