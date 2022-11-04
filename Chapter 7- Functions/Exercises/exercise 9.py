#exercise 9:Write a Python function to check whether a number falls in a given range.

def test_range(x):
    if x in range(3, 9):
        print(f" {x} is in the range")
    else :
        print(f" {x} The number is outside the given range.")
x = int(input("Enter a number: "))
test_range(x)