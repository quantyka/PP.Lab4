import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

degrees = float(input("Enter angle in degrees: "))
radians = degrees_to_radians(degrees)

print("Radians:", radians)