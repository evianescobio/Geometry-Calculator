import math

# This is the heading of the program.
print("==================")
print("Calculator for SHAPES📐")
print("==================\n")

# ---FORMULAS FOR AREA CALCULATION--- #
# Triangle Area Formula.
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


# --FORMULAS FOR PERIMETER CALCULATION-- #
# Triangle Perimeter #
def perimeter_triangle(side_a, side_b, side_c):
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


# Display Menu to Calculate Area.
def area_menu():
    while True:
        print("\n=== Area Calculator ===")
        print("1) Triangle")
        print("2) Rectangle")
        print("3) Square")
        print("4) Circle")
        print("5) Trapezoid")
        print("0) Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            b = float(input("Base: "))
            h = float(input("Height: "))
            print("Area =", round(area_triangle(b, h), 2))

        elif choice == "2":
            w = float(input("Width: "))
            h = float(input("Height: "))
            print("Area =", round(area_rectangle(w, h), 2))

        elif choice == "3":
            s = float(input("Side: "))
            print("Area =", round(area_square(s), 2))

        elif choice == "4":
            r = float(input("Radius: "))
            print("Area =", round(area_circle(r), 2))

        elif choice == "5":
            b1 = float(input("Base 1: "))
            b2 = float(input("Base 2: "))
            h = float(input("Height: "))
            print("Area =", round(area_trapezoid(b1, b2, h), 2))

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

# Display Menu to Calculate Perimeter.
def perimeter_menu():
    while True:
        print("\n=== Perimeter Calculator ===")
        print("1) Triangle")
        print("2) Rectangle")
        print("3) Square")
        print("4) Circle")
        print("5) Trapezoid")
        print("0) Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            a = float(input("Side A: "))
            b = float(input("Side B: "))
            c = float(input("Side C: "))
            print("Perimeter =", round(perimeter_triangle(a, b, c), 2))
        
        elif choice == "2":
            w = float(input("Width: "))
            h = float(input("Height: "))
            print("Perimeter =", round(perimeter_rectangle(w, h), 2))
        
        elif choice == "3":
            s = float(input("Side: "))
            print("Perimeter =", round(perimeter_square(s), 2))

        elif choice == "4":
            r = float(input("Radius: "))
            print("Perimeter =", round(perimeter_circle(r), 2))

        elif choice == "5":
            a = float(input("Side A: "))
            b = float(input("Side B: "))
            c = float(input("Side C: "))
            d = float(input("Side D: "))
            print("Perimeter =", round(perimeter_trapezoid(a, b, c, d), 2))
        
        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

# Display Menu to Calculate Volume.
def volume_menu():
    while True:
        print("\n=== Volume Calculator ===")
        print("1) Cube")
        print("2) Rectangular Prism")
        print("3) Cylinder")
        print("0) Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            s = float(input("Side: "))
            print("Volume =", round(volume_cube(s), 2))
        elif choice == "2":
            l = float(input("Length: "))
            w = float(input("Width: "))
            h = float(input("Height: "))
            print("Volume =", round(volume_rectangular_prism(l, w, h), 2))
        elif choice == "3":
            r = float(input("Radius: "))
            h = float(input("Height: "))
            print("Volume =", round(volume_cylinder(r, h), 2))
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


# Main Function
def main():
    while True:
        print("\n=== Main Menu ===")
        print("1) Calculate Area")
        print("2) Calculate Perimeter")
        print("3) Volume Calculator")
        print("0) Quit")

        main_choice = input("Choose an option: ").strip()

        if main_choice == "1":
            area_menu()
        elif main_choice == "2":
            perimeter_menu()
        elif main_choice == "3":
            volume_menu()
        elif main_choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()