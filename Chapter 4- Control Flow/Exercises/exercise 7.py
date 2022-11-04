#Excercise 7:Write a program to check whether the last digit of a number(enter by user)is divisible by 3 or not

num=int(input("enter any number "))
newnm=num%10
if newnm%3==0:
  print("the last digit of a number is divisible by 3")
else:
  print("the last digit of a number is not divisile by 3") 