#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return 0

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
                       }

    pre_v = 0
    output = 0
    for char in reversed(roman_string):
        v = roman_numerals.get(char,0)
        if v >= prev_v:
            output += v
        else:
            output -= v
        prev_v = v
    return output
