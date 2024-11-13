# Python code to demonstrate
# checking whether string
# is valid json or not

import json

# ini_string = '{"Geek" : 1,"forGeeks" : 2}'

a = '{"name":"John", "age":31, "Salary":25000}'
b = '{ "Subjects": {"Maths":85, "Physics":90}}'

# printing initial ini_string
print("initial strings given - \n", a, "\n", b)

# checking for string
try:
    json_object1 = json.loads(a)
    json_object2 = json.loads(b)
    print("Is valid json? true")

except ValueError as e:
    print("Is valid json? false")
