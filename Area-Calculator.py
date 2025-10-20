import math

# This is the heading of the program.
print("==================")
print("Area Calculator 📐")
print("==================\n")

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

# Main Function.
def main():
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
            print("Area = ", round(area_triangle(b, h), 2))

        elif choice == "2":
            w = float(input("Width: "))
            h = float(input("Height: "))
            print("Area = ", round(area_rectangle(w, h), 2))

        elif choice == "3":
            s = float(input("Side: "))
            print("Area = ", round(area_square(s), 2))

        elif choice == "4":
            r = float(input("Radius: "))
            print("Area = ", round(area_circle(r), 2))

        elif choice == "5":
            b1 = float(input("Base 1: "))
            b2 = float(input("Base 2: "))
            h = float(input("Height: "))
            print("Area = ", round(area_trapezoid(b1, b2, h), 2))

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()