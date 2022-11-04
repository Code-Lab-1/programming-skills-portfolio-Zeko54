#Excercise 6:Write a program to display sum of even numbers and odd numbers that fall between 12 and 37(including both numbers)

sum_of_odd=0
sum_of_even=0
for i in range(12,38):
  if i%2==0:
    sum_of_even=sum_of_even+i
  else:
    sum_of_odd=sum_of_odd+i
  
print("Sum of all even numbers is",sum_of_even)
print("Sum of all odd numbers is ",sum_of_odd)
