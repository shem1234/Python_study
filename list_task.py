# create a new file list_task.py
# trainees = ["John", [2, ["James","Mary"]]]
# 1. Display 2 from the list.
trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][0])

# 2. Output James  from the list.
print(trainees[1][1][0])

# 3. Using a method add 56 at the end of the list.
trainees.append(56)
print(trainees)

# 4. Using a method add the name Mike between James and Mary
print(trainees[1][1][0])
trainees[1][1].insert(1,"Mike")
print(trainees)

# 5. Change the value of 2 to 8
print(trainees[1])
trainees[1][0] = 8
print(trainees)

# 6. Remove John and Mary from the list.
trainees.pop(0)
print(trainees[0][1])
trainees[0][1].pop(2)
print(trainees)

# 7. Using a function, determine the length of the list
print(len(trainees))
