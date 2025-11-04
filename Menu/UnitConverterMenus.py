from Formulas.Areas import (area_triangle, area_rectangle, area_square, area_circle, area_trapezoid)
from Formulas.Perimeters import (perimeter_triangle, perimeter_rectangle, perimeter_square, perimeter_circle, perimeter_trapezoid)
from Formulas.Volumes import (volume_cube, volume_rectangular_prism, volume_cylinder)
from Unit_Converter.UnitConverter import (convert_units_area, convert_units_perimeter, convert_units_volume)



def converter_units_area_menu(value):
    print("Do you want to convert the units of the area result? (Y/N): ")
    choice = input().strip().lower()
    if choice in ('y', 'yes'):
        print("Enter the units you want to convert to:\n" \
              "1) mm²\n" \
              "2) cm²\n" \
              "3) m²\n" \
              "4) km²")
        to_unit_choice = input("Choose an option: ").strip()
        unit_map = {
            '1': 'mm²',
            '2': 'cm²',
            '3': 'm²',
            '4': 'km²'
        }
        if to_unit_choice in unit_map:
            result = convert_units_area(value, 'cm²', unit_map[to_unit_choice])
            print(f"Converted value = {round(result, 4)} {unit_map[to_unit_choice]}")
            return result
        else:
            print("Invalid option, no conversion will be performed.")
            return value
        

def converter_units_perimeter_menu(value):
    print("Do you want to convert the units of the perimeter result? (Y/N): ")
    choice = input().strip().lower()
    if choice in ('y', 'yes'):
        print("Enter the units you want to convert to:\n" \
              "1) mm\n" \
              "2) cm\n" \
              "3) m\n" \
              "4) km")
        to_unit_choice = input("Choose an option: ").strip()
        unit_map = {
            '1': 'mm',
            '2': 'cm',
            '3': 'm',
            '4': 'km'
        }
        if to_unit_choice in unit_map:
            result = convert_units_perimeter(value, 'cm', unit_map[to_unit_choice])
            print(f"Converted value = {round(result, 4)} {unit_map[to_unit_choice]}")
            return result
        else:
            print("Invalid option, no conversion will be performed.")
            return value
        
def converter_units_volume_menu(value):
    print("Do you want to convert the units of the volume result? (Y/N): ")
    choice = input().strip().lower()
    if choice in ('y', 'yes'):
        print("Enter the units you want to convert to:\n" \
              "1) mm³\n" \
              "2) cm³\n" \
              "3) m³\n" \
              "4) km³")
        to_unit_choice = input("Choose an option: ").strip()
        unit_map = {
            '1': 'mm³',
            '2': 'cm³',
            '3': 'm³',
            '4': 'km³'
        }
        if to_unit_choice in unit_map:
            result = convert_units_volume(value, 'cm³', unit_map[to_unit_choice])
            print(f"Converted value = {round(result, 4)} {unit_map[to_unit_choice]}")
            return result
        else:
            print("Invalid option, no conversion will be performed.")
            return value