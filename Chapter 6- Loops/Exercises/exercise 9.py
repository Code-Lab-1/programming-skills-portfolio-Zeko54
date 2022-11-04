#excercise 9:Display Fibonacci series up to 10 terms

num1, num2 = 0, 1

print("Fibonacci sequence:")

for x in range(10):
    
    print(num1 ,end=" ")
    
    a = num1 + num2

    
    num1 = num2
    num2 = a