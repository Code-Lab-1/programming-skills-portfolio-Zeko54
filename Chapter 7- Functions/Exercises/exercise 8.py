#exercise 8: Define a function in python that accepts 3 values and returns the maximum of three numbers.

def max(a, b, c):
    if a > b and a > c:
        print(f"{a} is maximum among all")
    elif b > a and b > c:
        print(f"{b} is maximum among all")
    else:
        print(f"{c} is maximum among all")

max(99,96,128)