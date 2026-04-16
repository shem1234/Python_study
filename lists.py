# create a list of fruits
fruits = ["Mango","Banana","Orange","Lemon"]
print(type(fruits))
print(fruits)
print(fruits[1])

# update items
fruits[1] = "Apple"
print(fruits)

# slice
print(fruits[1:3])

# skip items and print odd numbers
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0::2])

# reverse sequence
print(numbers[::-1])

# lists within a list
numbers=[1,2,3,4,["John","Peter","Alex"],5,6,7]
print(numbers[4:])
print(numbers[4][1:])
print(numbers[4][1:] + numbers[6:7])

# create a new file list_task.py
# trainees = ["John", [2, ["James","Mary"]]]
# 1. Display 2 from the list.
trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1:][0])


# 2. Output James  from the list.
print(trainees[1:])

# 3. Using a method add 56 at the end of the list.
trainees=trainees.append(56)
print(trainees)


# 4. Using a method add the name Mike between James and Mary
# 5. Change the value of 2 to 8
# 6. Remove John and Mary from the list.
# 7. Using a function, determine the length of the list
