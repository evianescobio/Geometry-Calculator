import math

# --VOLUME CALCULATION-- #
# Cube Volume Formula. #
def volume_cube(side):
    return side ** 3

# Rectangular Prism Volume Formula. #
def volume_rectangular_prism(length, width, height):
    return length * width * height

# Cylinder Volume Formula. #
def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height
