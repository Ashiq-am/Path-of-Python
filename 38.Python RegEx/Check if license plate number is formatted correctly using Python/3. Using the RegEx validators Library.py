import re

def validate_license_plate_with_library(plate, pattern):
  """
  This function validates a license plate against a given pattern using the built-in `re` module.
  """
  return re.match(pattern, plate) is not None  # Check if match object exists

# Example usage
us_pattern = r'^[A-Z]{3}-\d{4}$'
uk_pattern = r'^[A-Z]{2}\d{2} [A-Z]{3}$'

print(validate_license_plate_with_library('ABC-1234', us_pattern))  # True
print(validate_license_plate_with_library('AB12 CDE', uk_pattern))  # True
print(validate_license_plate_with_library('A1B-234', us_pattern))   # False
