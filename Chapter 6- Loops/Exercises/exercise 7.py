#Excercise 7:Write a program to display all numbers which are divisible by 11 but not by 2 between 100 and 500

for i in range(100,500):
  if i%11==0 and i%2!=0:
    print(i)
 