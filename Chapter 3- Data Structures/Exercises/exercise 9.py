#Excercise 9:Iterate both lists simultaneously

list_a = [5, 10, 15, 20]
list_b = [50, 100, 150, 200]

for x, y in zip(list_a, list_b[::-1]):
    print(x, y)