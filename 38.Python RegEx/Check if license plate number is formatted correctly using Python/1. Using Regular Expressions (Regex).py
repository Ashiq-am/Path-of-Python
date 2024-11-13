import re

def validate_license_plate(plate, pattern):
    regex = re.compile(pattern)
    if regex.match(plate):
        return True
    return False

# Example usage
us_pattern = r'^[A-Z]{3}-\d{4}$'  # Pattern for 'ABC-1234'
uk_pattern = r'^[A-Z]{2}\d{2} [A-Z]{3}$'  # Pattern for 'AB12 CDE'

print(validate_license_plate('ABC-1234', us_pattern))  # True
print(validate_license_plate('AB12 CDE', uk_pattern))  # True
print(validate_license_plate('A1B-234', us_pattern))   # False
