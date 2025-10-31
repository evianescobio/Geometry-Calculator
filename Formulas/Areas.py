import math

# ---FORMULAS FOR AREA CALCULATION--- #
# Triangle Area Formula #
def area_triangle(base, height):
    return 0.5 * base * height

# Rectangle Area Formula.
def area_rectangle(width, height):
    return width * height

# Square Area Formula.
def area_square(side):
    return side * side

# Circle Area Formula.
def area_circle(radius):
    return math.pi * radius * radius

# Trapezoid Area Formula.
def area_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height