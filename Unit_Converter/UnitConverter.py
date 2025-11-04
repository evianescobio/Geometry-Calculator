# This module provides functions to convert between different units of area, perimeter, and volume. #

def convert_units_area(value, from_unit, to_unit):
    # Conversion factors to square meters #
    conversion_factors = {
        'cm²': 0.0001,
        'm²': 1,
        'km²': 1000000,
        'in²': 0.00064516,
        'ft²': 0.092903,
        'yd²': 0.836127,
        'ac': 4046.86,
        'ha': 10000
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported unit for area conversion!")

    # Convert to square meters first, then to the target unit
    value_in_square_meters = value * conversion_factors[from_unit]
    return value_in_square_meters / conversion_factors[to_unit]

def convert_units_perimeter (value, from_unit, to_unit):
    # Conversion factors to meters #
    conversion_factors = {
        'cm': 0.01,
        'm': 1,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported unit for perimeter conversion!")
    # Convert to meters first, then to the target unit
    value_in_meters = value * conversion_factors[from_unit]
    return value_in_meters / conversion_factors[to_unit]

def convert_units_volume(value, from_unit, to_unit):
    # Conversion factors to cubic meters #
    conversion_factors = {
        'cm³': 0.000001,
        'm³': 1,
        'km³': 1000000000,
        'in³': 0.0000163871,
        'ft³': 0.0283168,
        'yd³': 0.764555,
        'L': 0.001,
        'mL': 0.000001
    }

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported unit for volume conversion!")
    # Convert to cubic meters first, then to the target unit
    value_in_cubic_meters = value * conversion_factors[from_unit]
    return value_in_cubic_meters / conversion_factors[to_unit]

