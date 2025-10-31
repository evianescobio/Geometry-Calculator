import math

# --FORMULAS FOR PERIMETER CALCULATION-- #
# Triangle Perimeter #
def perimeter_triangle(side_a, side_b, side_c):
    # Check if sides can form a valid triangle
    if (side_a + side_b <= side_c) or (side_b + side_c <= side_a) or (side_a + side_c <= side_b):
        raise ValueError("These sides cannot form a valid triangle!")
    return side_a + side_b + side_c

# Rectangle Perimeter #
def perimeter_rectangle(width, height):
    return 2 * (width + height)

# Square Perimeter #
def perimeter_square(side):
    return 4 * side

# Circle Perimeter #
def perimeter_circle(radius):
    return 2 * math.pi * radius

# Trapezoid Perimeter #
def perimeter_trapezoid(side_a, side_b, side_c, side_d):
    return side_a + side_b + side_c + side_d
