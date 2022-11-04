#exercise 6:Take a number from user and print its table upto 10

def table():
  num=int(input("Enter the number="))
  for i in range(1,11):

    mul=num*i
    print(num ,'x' , i , '=', mul)
table()    