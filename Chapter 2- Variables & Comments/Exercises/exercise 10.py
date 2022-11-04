#exercise 10:Print the sum of the current number and the previous number

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

for x in range(1, 10):
    sum = previous_num + x
    print("Current Number:", x, "Previous Number:", previous_num, " Sum:", sum)
    
    previous_num = x