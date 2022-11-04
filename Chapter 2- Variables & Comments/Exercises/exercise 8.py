#exercise 8:Write a python program to read three numbers and find the smallest among them

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if(num1 < num2) and (num1 < num3):
  print("The smallest number is" ,num1)
elif(num2 < num1) and (num2<num3):
  print("The smallest number is" ,num2)
else:
  print("The smallest number is" ,num3)