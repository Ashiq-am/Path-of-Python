def validate_license_plate_simple(plate):
    if len(plate) == 8 and plate[:3].isalpha() and plate[3] == '-' and plate[4:].isdigit():
        return True
    return False

# Example usage
print(validate_license_plate_simple('ABC-1234'))  # True
print(validate_license_plate_simple('AB12 CDE'))  # False
