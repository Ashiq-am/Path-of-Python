# Function to check if casting is possible or not
def can_cast(source_type, dest_type):
    try:
        dest_type(source_type())
        return True

    except ValueError:
        return False

# Driving Code
print(can_cast(int, float))
print(can_cast(float, int))
print(can_cast(str, int))
print(can_cast(int, str))
print(can_cast(float,str))
print(can_cast(str,float))
