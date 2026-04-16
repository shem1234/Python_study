# append - adds items at the end of the list
my_list = ["Mike","Jane","Alex",1000,200,2000,True,False]
my_list.append("Donkey")
print(my_list)

# insert - adds an item at a specific index
my_list.insert(1,"Mary")
print(my_list)

# pop - removes an item at a specific index. if no 
# index is inserted, it removes the last item 
my_list.pop(3)
print(my_list)

# task
lst=[10,20,30,["Jane","Mary",[1000,2000,3000]],40,50,60]
print(lst)

# using methods
# add 70 at the end of the list
lst.append(70)
print(lst)

# add 1500 between 1000 and 2000
print(lst[3])
print(lst[3][2])
lst[3][2].insert(1,1500)
print(lst)

# delete 2000
print(lst[3])
print(lst[3][2])
lst[3][2].pop(2)
print(lst)

# sort
list1 = [1,50,10,20,5,2]
list1.sort()

# extend
list2 = ["Mike","Jane","Alex"]
list1 = [1,50,10,20,5,2]
list3 = list1 + list2
list2.extend(list1)
print(list3)

# count
print(list2.count("Mike"))

# copy
list4 = list1.copy()
print(list4)

# clear
my_list.clear()
print(my_list)

# in memebrship
list2 = ["Mike","Jane","Alex"]
print("Alex" in list2)