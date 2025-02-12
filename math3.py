import math

def regular_polygon_area(sides, length):
    return (sides * length**2) / (4 * math.tan(math.pi / sides))

sides = int(input("Enter the number of sides: "))
length = float(input("Enter the length of each side: "))

print("Area of the regular polygon:", regular_polygon_area(sides, length))