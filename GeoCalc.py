import math

from Formulas.Areas import (area_triangle, area_rectangle, area_square, area_circle, area_trapezoid)

from Formulas.Perimeters import (perimeter_triangle, perimeter_rectangle, perimeter_square, perimeter_circle, perimeter_trapezoid)

from Formulas.Volumes import (volume_cube, volume_rectangular_prism, volume_cylinder)

from Menu.Menus import (area_menu, perimeter_menu, volume_menu)

# This is the heading of the program.
print("==================")
print("Calculator for SHAPES📐")
print("==================")

# Main Function
def main():
    while True:
        print("\n=== Main Menu ===")
        print("1) Calculate Area")
        print("2) Calculate Perimeter")
        print("3) Calculate Volume")
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