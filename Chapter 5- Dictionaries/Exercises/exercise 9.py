#Excercise 9:Write a code to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square 
# of keys

a=dict()
for x in range(1,16):
    a[x]=x**2
print(a)