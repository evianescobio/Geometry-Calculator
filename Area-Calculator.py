import math

# This is the heading of the program.
print("==================")
print("Area Calculator 📐")
print("==================\n")

# Function for the area of a triangle.
def area_triangle(base, height):
    return 0.5 * base * height

# Function for the area of a rectangle.
def area_rectangle(width, height):
    return width * height

# Function for the area of a square.
def area_square(side):
    return side * side

# Function for ther area of a circle.
def area_circle(radius):
    return math.pi * radius * radius

# Main Function.
def main():
    while True:
        print("\n=== Area Calculator ===")
        print("1) Triangle")
        print("2) Rectangle")
        print("3) Square")
        print("4) Circle")
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
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()