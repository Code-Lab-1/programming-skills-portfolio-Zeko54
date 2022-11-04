#exercise 10:Define a function that accepts radius and returns the area of a circle.

def area(radius):
    area = 3.14*radius*radius
    return area

radius = int(input("Enter the radius: "))  
print(area(radius))
