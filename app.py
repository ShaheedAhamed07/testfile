import math

def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2

# Get input from the user
print("Welcome to the Circle Area Calculator!")
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
if radius < 0:
    print("Radius cannot be negative. Please enter a valid number.")
else:
    area = calculate_circle_area(radius)
    print(f"The area of the circle with radius {radius} is {area:.2f}.")
