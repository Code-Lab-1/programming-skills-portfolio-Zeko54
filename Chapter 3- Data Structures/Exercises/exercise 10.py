#Excercise 10:Add new item to list after a specified item write a program to add item 7000 after 6000 in the following Python List

list1 = [1000, 2000, [3000, 4000, [5000, 6000], 500], 300, 400]


list1[2][2].append(7000)
print(list1)