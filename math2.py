def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

base1 = float(input("Enter first base: "))
base2 = float(input("Enter second base: "))
height = float(input("Enter height: "))

print("Area of the trapezoid:", trapezoid_area(base1, base2, height))