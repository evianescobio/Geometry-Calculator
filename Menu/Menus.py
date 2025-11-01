import math

from Formulas.Areas import (area_triangle, area_rectangle, area_square, area_circle, area_trapezoid)

from Formulas.Perimeters import (perimeter_triangle, perimeter_rectangle, perimeter_square, perimeter_circle, perimeter_trapezoid)

from Formulas.Volumes import (volume_cube, volume_rectangular_prism, volume_cylinder)

# Display Menu to Calculate Area. #
def area_menu():
    while True:
        print("\n=== Area Calculator ===")
        print("1) Triangle")
        print("2) Rectangle")
        print("3) Square")
        print("4) Circle")
        print("5) Trapezoid")
        print("0) Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                b = float(input("Base (cm): "))
                h = float(input("Height (cm): "))
                print("\nArea =", round(area_triangle(b, h), 2))
                # Ask whether to repeat or return to main menu.
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")

        elif choice == "2":
            try:
                w = float(input("Width (cm): "))
                h = float(input("Height (cm): "))
                print("\nArea =", round(area_rectangle(w, h), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")

        elif choice == "3":
            try:
                s = float(input("Side (cm): "))
                print("\nArea =", round(area_square(s), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")

        elif choice == "4":
            try:
                r = float(input("Radius (cm): "))
                if r <= 0:
                    print("Error: Radius must be a positive number!")
                    continue
                print("\nArea =", round(area_circle(r), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter a valid number!")

        elif choice == "5":
            try:
                b1 = float(input("Base 1 (cm): "))
                b2 = float(input("Base 2 (cm): "))
                h = float(input("Height (cm): "))
                print("\nArea =", round(area_trapezoid(b1, b2, h), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")

        elif choice == "0":
            break

        else:
            print("Invalid option, please try again.")



# Display Menu to Calculate Perimeter. #
def perimeter_menu():
    while True:
        print("\n=== Perimeter Calculator ===")
        print("1) Triangle")
        print("2) Rectangle")
        print("3) Square")
        print("4) Circle")
        print("5) Trapezoid")
        print("0) Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                a = float(input("Side A (cm): "))
                b = float(input("Side B (cm): "))
                c = float(input("Side C (cm): "))
                if any(side <= 0 for side in [a, b, c]):
                    print("Error: All sides must be positive numbers!")
                    continue
                print("\nPerimeter =", round(perimeter_triangle(a, b, c), 2))
                if not back_to_main_menu():
                    break
            except ValueError as e:
                # perimeter_triangle may raise a ValueError for invalid triangle sides. #
                if str(e).startswith("These sides"):
                    print(e)
                else:
                    print("Error: Please enter valid numbers!")
        
        elif choice == "2":
            try:
                w = float(input("Width (cm): "))
                h = float(input("Height (cm): "))
                print("\nPerimeter =", round(perimeter_rectangle(w, h), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")

        elif choice == "3":
            try:
                s = float(input("Side (cm): "))
                print("\nPerimeter =", round(perimeter_square(s), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")

        elif choice == "4":
            try:
                r = float(input("Radius (cm): "))
                print("\nPerimeter =", round(perimeter_circle(r), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")

        elif choice == "5":
            try:
                a = float(input("Side A (cm): "))
                b = float(input("Side B (cm): "))
                c = float(input("Side C (cm): "))
                d = float(input("Side D (cm): "))
                print("\nPerimeter =", round(perimeter_trapezoid(a, b, c, d), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")
        
        elif choice == "0":
            break

        else:
            print("Invalid option, please try again.")



# Display Menu to Calculate Volume. #
def volume_menu():
    while True:
        print("\n=== Volume Calculator ===")
        print("1) Cube")
        print("2) Rectangular Prism")
        print("3) Cylinder")
        print("0) Back to Main Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                s = float(input("Side (cm): "))
                print("\nVolume =", round(volume_cube(s), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")
        elif choice == "2":
            try:
                l = float(input("Length (cm): "))
                w = float(input("Width (cm): "))
                h = float(input("Height (cm): "))
                print("\nVolume =", round(volume_rectangular_prism(l, w, h), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")
        elif choice == "3":
            try:
                r = float(input("Radius (cm): "))
                h = float(input("Height (cm): "))
                print("\nVolume =", round(volume_cylinder(r, h), 2))
                if not back_to_main_menu():
                    break
            except ValueError:
                print("Error: Please enter valid numbers!")
        elif choice == "0":
            break
        else:
            print("Invalid option, please try again.")



# Loop back to main menu after each calculation. #
def back_to_main_menu():
    while True:
        choice = input("\nDo you want to do another calculation in this menu?(Y/N): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        if choice in ("n", "no"):
            return False
        print("Invalid option. Please enter 'Y' to repeat or 'N' to return to the main menu.")
    
